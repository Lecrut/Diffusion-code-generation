def main():
    my_list = [10, 20, 30, 40, 50]
    print("Original List:", my_list)
    print("\nAccessing elements using positive indices:")
    print("Element at index 0:", my_list[0])
    print("Element at index 2:", my_list[2])
    print("Element at index 4:", my_list[4])
    print("\nAccessing elements using negative indices:")
    print("Element at index -1 (last element):", my_list[-1])
    print("Element at index -2 (second to last):", my_list[-2])
    print("Element at index -5 (first element):", my_list[-5])
    print("\nSlicing examples:")
    print("Slice from index 1 to 3 (exclusive):", my_list[1:4])
    print("Slice from the beginning to index 3:", my_list[:3])
    print("Slice from index 2 to the end:", my_list[2:])
    print("Slice using a step (every second element):", my_list[::2])
if __name__ == '__main__':
    main()