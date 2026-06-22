class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
        else:
            new_node = Node(value)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def min_value(self):
        if not self.head:
            return None
        current = self.head
        minimum = current.value
        while current.next != self.head:
            if current.next.value < minimum:
                minimum = current.next.value
            current = current.next
        return minimum

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

if __name__ == '__main__':
    clist = CircularLinkedList()
    clist.append(5)
    clist.append(2)
    clist.append(8)
    clist.append(1)
    clist.append(9)
    clist.append(3)
    clist.append(7)
    print("Minimum value:", clist.min_value())