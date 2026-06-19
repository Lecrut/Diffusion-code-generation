class AdjacentComparison:
    @staticmethod
    def compare_adjacent_elements(lst):
        if len(lst) < 2:
            return
        previous = lst[0]
        for current in lst[1:]:
            yield previous <= current
            previous = current

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7, 9]
    sample_input_2 = [1, 3, 2, 5]
    
    results_1 = list(AdjacentComparison.compare_adjacent_elements(sample_input_1))
    results_2 = list(AdjacentComparison.compare_adjacent_elements(sample_input_2))
    
    print(results_1)
    print(results_2)