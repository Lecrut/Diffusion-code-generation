if __name__ == '__main__':
    LIST1 = [1, 2, 3]
    LIST2 = [4, 5, 6]
    
    def append_lists(dest_list, src_list):
        dest_list += src_list
    
    append_lists(LIST1, LIST2)
    print("Updated List 1:", LIST1)