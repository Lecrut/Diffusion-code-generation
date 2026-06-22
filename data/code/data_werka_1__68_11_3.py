def absolute_difference_generator(list1, list2):
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    sample_data = {
        'list1': [7, 14, 21, 28],
        'list2': [3, 6, 9, 12]
    }
    
    for diff in absolute_difference_generator(sample_data['list1'], sample_data['list2']):
        print(diff)