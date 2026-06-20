def validate_input(*iterables):
    if not iterables:
        raise ValueError("No iterables provided")
    for iterable in iterables:
        if not isinstance(iterable, (list, tuple, set)):
            raise TypeError(f"Invalid input: {iterable}. Expected list, tuple, or set")

def is_mutually_exclusive(*iterables):
    validate_input(*iterables)
    elements = set()
    for iterable in iterables:
        if any(element in elements for element in iterable):
            return False
        elements.update(iterable)
    return True

if __name__ == '__main__':
    sample_constraints_1 = [1, 2, 3]
    result_1 = is_mutually_exclusive(sample_constraints_1)
    print(f"Constraints: {sample_constraints_1}, Mutual Exclusivity: {result_1}")
    
    sample_constraints_2 = [1, 2, 1]
    result_2 = is_mutually_exclusive(sample_constraints_2)
    print(f"Constraints: {sample_constraints_2}, Mutual Exclusivity: {result_2}")
    
    sample_constraints_3 = [5, 8, 10]
    result_3 = is_mutually_exclusive(sample_constraints_3)
    print(f"Constraints: {sample_constraints_3}, Mutual Exclusivity: {result_3}")

    sample_constraints_4 = [[1, 2], [3, 4]]
    result_4 = is_mutually_exclusive(sample_constraints_4)
    print(f"Constraints: {sample_constraints_4}, Mutual Exclusivity: {result_4}")

    sample_constraints_5 = [(1, 2), (3, 4)]
    result_5 = is_mutually_exclusive(sample_constraints_5)
    print(f"Constraints: {sample_constraints_5}, Mutual Exclusivity: {result_5}")