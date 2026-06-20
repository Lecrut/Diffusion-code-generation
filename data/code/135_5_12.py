class ListCompComparator:
    def generate_comprehension(self, start, end, func):
        return [func(x) for x in range(start, end)]
    
    def compare_comps(self, comp1, comp2):
        return set(comp1) == set(comp2)

if __name__ == '__main__':
    comparator = ListCompComparator()
    sample_start = 0
    sample_end = 5
    func1 = lambda x: x**2
    func2 = lambda x: x*x
    
    comp1 = comparator.generate_comprehension(sample_start, sample_end, func1)
    comp2 = comparator.generate_comprehension(sample_start, sample_end, func2)
    
    result = comparator.compare_comps(comp1, comp2)
    print(result)