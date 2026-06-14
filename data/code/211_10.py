import timeit
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
intersection = set_a.intersection(set_b)
symmetric_difference = set_a.symmetric_difference(set_b)
if __name__ == '__main__':
    start_time = timeit.default_timer()
    result_intersection = set_a.intersection(set_b)
    result_symmetric_difference = set_a.symmetric_difference(set_b)
    end_time = timeit.default_timer()
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Intersection: {result_intersection}")
    print(f"Symmetric Difference (A - B): {result_symmetric_difference}")
    print(f"Time taken for operations: {(end_time - start_time):.6f} seconds")