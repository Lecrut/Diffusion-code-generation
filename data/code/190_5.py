class MyList:
    def contains(self, item):
        return item in self.data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    list_object = MyList()
    list_object.data = sample_list
    print(f"Checking for item 3 in {sample_list}: {list_object.contains(3)}")
    print(f"Checking for item 9 in {sample_list}: {list_object.contains(9)}")
    print(f"Checking for item 1 in {empty_list}: {list_object.contains(1)}")
    print(f"Checking for item 0 in {empty_list}: {list_object.contains(0)}")