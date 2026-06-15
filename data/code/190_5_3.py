class MyList:
    def contains(self, item):
        return item in self.data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    list_object = MyList()
    list_object.data = sample_list
    print(f"Checking for 30 in {sample_list}: {list_object.contains(30)}")
    print(f"Checking for 99 in {sample_list}: {list_object.contains(99)}")
    print(f"Checking for 10 in {sample_list}: {list_object.contains(10)}")
    list_object.data = empty_list
    print(f"Checking for 5 in {empty_list}: {list_object.contains(5)}")