"""
we use an optimizer to adjust the parameters
of our network based on the gradients computed
during back propagation
"""
from turabnet.nn import NeuralNet

class Optimizer:
    def step(self, net: NeuralNet) -> None:
        raise NotImplementedError


class SGD(Optimizer):
    def __init__(self, lr: float = 0.01) -> None:
        self.lr = lr

    def step(self, net: NeuralNet) -> None:
        """
        loops over each param {w, b} and update
        """
        for param, grad in net.params_and_grads():
            param -= self.lr * grad






