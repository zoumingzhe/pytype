"""Test cases that need solve_unknowns."""

from pytype.tests import test_inference


class SolverTests(test_inference.InferenceTest):

  def testAmbiguousAttr(self):
    with self.Infer("""
      class Node(object):
          children = ()
          def __init__(self):
              self.children = []
              for ch in self.children:
                  pass
    """, deep=True, solve_unknowns=True, extract_locals=True) as ty:
      self.assertTypesMatchPytd(ty, """
      class Node:
        children = list or tuple
        def __init__(self) -> NoneType
      """)
