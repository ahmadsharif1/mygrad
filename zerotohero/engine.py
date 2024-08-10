class Value:
  def __init__(self, data, _children=(), _op=''):
    self.data = data
    self._prev = set(_children)
    self._op = _op

  def __add__(self, other):
    out = Value(self.data + other.data, (self, other), '+')
    return out
  
  def __mul__(self, other):
    out = Value(self.data * other.data, (self, other), '*')
    return out
  
  def __repr__(self) -> str:
    return f"{self.data=}"
  
if __name__ == "__main__":
  a = Value(2.0)
  b = Value(3.0)
  #c = a / b
  print(a + b)
  print(a * b)
