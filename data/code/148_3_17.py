LARGEST_DEFAULT = float('-inf')

def find_largest(data):
    if not data:
        return LARGEST_DEFAULT
    return max(data)

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8]
    print(f"Largest in {sample_data1}: {find_largest(sample_data1)}")
    
    sample_data2 = [-5, -1, -10, -2]
    print(f"Largest in {sample_data2}: {find_largest(sample_data2)}")
    
    sample_data3 = [3.14, 2.71, 1.618]
    print(f"Largest in {sample_data3}: {find_largest(sample_data3)}")
    
    sample_data4 = [42]
    print(f"Largest in {sample_data4}: {find_largest(sample_data4)}")