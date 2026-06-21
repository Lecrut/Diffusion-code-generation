def reverse_integers_in_list(list_of_integers):
    return list(reversed(list_of_integers))

if __name__ == '__main__':
    input_list = [123, 456, 789]
    output = reverse_integers_in_list(input_list)
    print(output)