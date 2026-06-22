def absolute_difference_generator(list1, list2):
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    data = {
        'list1': [100, 200, 300],
        'list2': [90, 180, 270]
    }
    for diff in absolute_difference_generator(data['list1'], data['list2']):
        print(diff)