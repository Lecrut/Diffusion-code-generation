class ListAppender:
    def __init__(self):
        self.list1 = [1, 2, 3]
        self.list2 = [4, 5, 6]

    def append_lists(self):
        self.list1 += self.list2

if __name__ == '__main__':
    appender = ListAppender()
    appender.append_lists()
    print("Updated List 1:", appender.list1)