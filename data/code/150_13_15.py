def remove_target(data, target):
    return [item for item in data if item != target]

if __name__ == '__main__':
    initial_list = ['apple', 'banana', 'cherry', 'apple']
    target_fruit = 'apple'
    result_list = remove_target(initial_list, target_fruit)
    print(result_list)