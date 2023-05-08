def func(z): return sum(int(i) for i in z)

class Test_One(__import__('unittest').TestCase):
    def test_sum_list_int(self): self.assertEqual(func([1,4,5]), 10)
    def test_sum_list_str(self): self.assertEqual(func(['1','4','5']), 10)
    def test_sum_list_uncommon(self): self.assertEqual(func(['1','2', 3, '2', 2]), 10)
    def test_sum_tuple_int(self): self.assertEqual(func(tuple(i for i in range(0,5))), 10)
    def test_sum_tuple_str(self): self.assertEqual(func(tuple(str(i) for i in range(0,5))), 10)
    def test_sum_tuple_uncommon(self): self.assertEqual(func(('1','2', 3, '2', 2)), 10)
if __name__ == '__main__': __import__('unittest').main()