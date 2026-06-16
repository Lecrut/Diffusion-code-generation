if __name__ == '__main__':
    data = [1, 5, 2, 8, 3]
    def iterative_sum(numbers):
        total = 0
        for number in numbers:
            total += number
        return total
    result_iterative = iterative_sum(data)
    def functional_sum(numbers):
        return sum(numbers)
    result_functional = functional_sum(data)
    print(f"Sample List: {data}")
    print(f"Result from Iterative Approach: {result_iterative}")
    print(f"Result from Functional Approach (sum()): {result_functional}")