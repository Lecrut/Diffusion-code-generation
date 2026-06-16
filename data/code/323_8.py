if __name__ == '__main__':
    input_list = [1, 5, 2, 8, 3]
    differences = [input_list[i+1] - input_list[i] for i in range(len(input_list) - 1)]
    print(differences)