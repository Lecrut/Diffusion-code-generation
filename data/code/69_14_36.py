MAX_INDEX = 4

def access_elements_by_index(sample_list):
    for index in range(MAX_INDEX + 1):
        if index < len(sample_list):
            print(sample_list[index])
        else:
            print("Index out of bounds")

if __name__ == '__main__':
    sample_values = [7, 17, 27, 37, 47]
    access_elements_by_index(sample_values)