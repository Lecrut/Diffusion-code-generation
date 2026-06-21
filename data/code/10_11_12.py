class ArrayAccessHelper:
    def get_first(self, data):
        if not data:
            return None
        return data[0]

if __name__ == '__main__':
    helper = ArrayAccessHelper()
    print(helper.get_first([1, 2, 3]))
    print(helper.get_first([]))
    print(helper.get_first([99]))