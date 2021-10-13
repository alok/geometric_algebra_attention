
from .. import base
from .VectorAttention import VectorAttention

class Vector2VectorAttention(base.Vector2VectorAttention, VectorAttention):
    __doc__ = base.Vector2VectorAttention.__doc__

    def __init__(self, score_net, value_net, scale_net, reduce=True,
                 merge_fun='mean', join_fun='mean', rank=2,
                 invariant_mode='single', covariant_mode='partial',
                 **kwargs):
        base.Vector2VectorAttention.__init__(self, scale_net=scale_net)
        VectorAttention.__init__(
            self, score_net=score_net, value_net=value_net,
            reduce=reduce, merge_fun=merge_fun, join_fun=join_fun, rank=rank,
            invariant_mode=invariant_mode, covariant_mode=covariant_mode,
            **kwargs)

    @classmethod
    def from_config(cls, config):
        new_config = dict(config)
        for key in ('scale_net',):
            new_config[key] = keras.models.Sequential.from_config(new_config[key])
        return super(Vector2VectorAttention, cls).from_config(new_config)

    def get_config(self):
        result = super().get_config()
        result['scale_net'] = self.scale_net.get_config()
        return result
