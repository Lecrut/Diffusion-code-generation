if __name__ == '__main__':
    data = [1, 5, 2, 8, 3]
    def iterative_sum(lst):
        total = 0
        for item in lst:
            total += item
        return total
    result_iterative = iterative_sum(data)
    def functional_sum(lst):
        return sum(lst)
    result_functional = functional_sum(data)
    print(f"Sample List: {data}")
    print(f"Iterative Sum Result: {result_iterative}")
    print(f"Functional Sum Result: {result_functional}")