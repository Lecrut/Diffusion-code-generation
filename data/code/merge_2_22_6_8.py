import sys
def delete_by_index(sequence, index):
    if isinstance(sequence, str):
        return sequence[:index] + sequence[index+1:]
    elif isinstance(sequence, list):
        new_list = []
        for i in range(len(sequence)):
            if i != index:
                new_list.append(sequence[i])
        return new_list
if __name__ == '__main__':
    string_input = "Hello World"
    list_input = [10, 20, 30, 40]
    print(f"Original String: {string_input}")
    deleted_string = delete_by_index(string_input, 6)
    print(f"After deleting index 6 (space): '{deleted_string}'")
    print(f"\nOriginal List: {list_input}")
    deleted_list = delete_by_index(list_input, 2)
    print(f"After deleting index 2 (30): {deleted_list}")