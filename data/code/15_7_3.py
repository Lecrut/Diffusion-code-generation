my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 40}
key1 = 'a'
key2 = 'c'
result_dict = {
    'are_equal': my_dict[key1] == my_dict[key2]
}
if __name__ == '__main__':
    print(result_dict)