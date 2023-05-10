from abc import ABC, abstractmethod


class Blinkable(ABC):
    """
    We can use an Abstract Base Class (ABC) to create an interface.
    The interface is an abstract method. It has no real implementation,
    it can simply contain pass. It must, however, by implemented
    by subclasses that promise to implement it.
    """
    @abstractmethod
    def blink(self):
        pass
