class Test:
  def assert_equals(a, b, *args, **kwargs):
    assert a == b
    print('Passed')
  def assertEquals(a, b, *args, **kwargs):
    assert_equals(a, b, *args, **kwargs)
  def assertNotEquals(a, b, *args, **kwargs):
    assert a != b
    print('Passed')    