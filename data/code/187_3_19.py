MAX_FLOAT = float('inf')

def find_largest(data):
    return max(data) if data else MAX_FLOAT

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    sample_list4 = []
    
    print(f"The largest value in {sample_list1} is: {find_largest(sample_list1)}")
    print(f"The largest value in {sample_list2} is: {find_largest(sample_list2)}")
    print(f"The largest value in {sample_list3} is: {find_largest(sample_list3)}")
    print(f"The largest value in an empty list is: {find_largest(sample_list4)}")