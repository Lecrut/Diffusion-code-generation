class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next and current.next.data != key:
            current = current.next
        if current and current.next:
            current.next = current.next.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.prepend(0)
    print("After append and prepend:", [node.data for node in (linked_list.head, linked_list.head.next, linked_list.head.next.next)])
    linked_list.delete(1)
    print("After delete 1:", [node.data for node in (linked_list.head, linked_list.head.next)])
    found = linked_list.search(2)
    print("Search for 2:", found)