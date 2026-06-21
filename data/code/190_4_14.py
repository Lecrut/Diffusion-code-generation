class TupleChecker:
    def __init__(self, data):
        self.data = data

    def check_existence(self, target):
        return target in self.data

if __name__ == '__main__':
    checker1 = TupleChecker([1, 2, 3, 4, 5])
    target1 = 3
    print(f"List: {checker1.data}, Target: {target1} -> Result: {checker1.check_existence(target1)}")
    
    checker2 = TupleChecker([10, 20, 30])
    target2 = 5
    print(f"List: {checker2.data}, Target: {target2} -> Result: {checker2.check_existence(target2)}")

    checker3 = TupleChecker(['a', 'b', 'c'])
    target3 = 'd'
    print(f"List: {checker3.data}, Target: {target3} -> Result: {checker3.check_existence(target3)}")