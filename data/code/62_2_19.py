if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    element_map = {'second': lambda lst: lst[1]}
    result = element_map['second'](my_list)
    print(result)