def sort_tuples_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [
        [(1, 2), (3, 4), (5, 6)],
        [(7, 1), (9, 3), (8, 2)],
        [(4, 3), (2, 1), (5, 0)],
        [(10, 10)],
        []
    ]
    for data in sample_data:
        print(f"Sorted {data}: {sort_tuples_by_second_element(data)}")