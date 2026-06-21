class ListReverser:
    def reverse_list(self, input_list):
        reversed_list = []
        start = 0
        end = len(input_list) - 1
        while start <= end:
            reversed_list.append(input_list[end])
            end -= 1
        return reversed_list

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list_1 = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list_1}")
    print(f"Reversed list: {reverser.reverse_list(sample_list_1)}")
    
    sample_list_2 = ['a', 'b', 'c', 'd']
    print(f"Original list: {sample_list_2}")
    print(f"Reversed list: {reverser.reverse_list(sample_list_2)}")
    
    sample_list_3 = [10, 20, 30]
    print(f"Original list: {sample_list_3}")
    print(f"Reversed list: {reverser.reverse_list(sample_list_3)}")