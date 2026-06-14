import sys
if __name__ == '__main__':
    input_data = [
        [1, 2, 3],
        [10, 20, 30, 40],
        [5, 5, 5]
    ]
    for data_set in input_data:
        if data_set:
            average = sum(data_set) / len(data_set)
            print(average)