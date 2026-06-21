class Checklist:
    def __init__(self, members):
        self.members = sorted(members)

    def binary_search(self, target):
        low, high = 0, len(self.members) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.members[mid] == target:
                return True
            elif self.members[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    checklist = Checklist([1, 5, 2, 8, 3])
    print(f"Membership: {checklist.binary_search(8)}")
    print(f"Membership: {checklist.binary_search(9)}")
    
    checklist_str = Checklist(['a', 'b', 'c'])
    print(f"Membership: {checklist_str.binary_search('c')}")
    print(f"Membership: {checklist_str.binary_search('d')}")
    
    checklist_num = Checklist([10, 20, 30])
    print(f"Membership: {checklist_num.binary_search(20)}")
    print(f"Membership: {checklist_num.binary_search(25)}")