class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def access_elements(self, *indices):
        return [self.elements[i] for i in indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    
    print("Accessing elements using positive indices:")
    print("Element at index 0:", accessor.access_elements(0)[0])
    print("Element at index 2:", accessor.access_elements(2)[0])
    print("Element at the last index (index -1):", accessor.access_elements(-1)[0])
    
    print("\nAccessing elements using negative indices:")
    print("Element at index -1 (last element):", accessor.access_elements(-1)[0])
    print("Element at index -3:", accessor.access_elements(-3)[0])
    
    print("\nSlicing examples:")
    print("Slice from index 1 to 3 (exclusive):", accessor.elements[1:4])
    print("Slice from the beginning to index 3:", accessor.elements[:3])
    print("Slice from index 2 to the end:", accessor.elements[2:])
    print("Slice using a step (every second element):", accessor.elements[::2])