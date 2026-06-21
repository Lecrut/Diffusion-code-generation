MAX_INT = float('-inf')

def find_largest(data):
    return max(data) if data else MAX_INT

if __name__ == '__main__':
    sample_list_1 = [10, 5, 22, 8, 30]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"List: {sample_list_1}, Largest: {find_largest(sample_list_1)}")
    print(f"List: {sample_list_2}, Largest: {find_largest(sample_list_2)}")
    print(f"List: {sample_list_3}, Largest: {find_largest(sample_list_3)}")
    print(f"List: {sample_list_4}, Largest: {find_largest(sample_list_4)}")