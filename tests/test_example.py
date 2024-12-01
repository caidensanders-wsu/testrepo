def add(a, b):
  return a + b

def test_add_1():
  assert add(1, 2) == 3

def test_add_2():
  assert add(1, -2) == -1

def test_add_3():
  assert add(-1, -1) == -2

def test_add_4():
  assert add(-1, 8) == 7

def test_add_5():
  assert add(200, 200) == 400
