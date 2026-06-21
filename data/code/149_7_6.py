def reverse_integers_in_list(list_of_integers):
    reversed_list = []
    for i in list_of_integers:
        reversed_i = int(str(i)[::-1])
        reversed_list.append(reversed_i)
    return reversed_list

if __name__ == '__main__':
    input_list = [123, 456, 789]
    output = reverse_integers_in_list(input_list)
    print(output)