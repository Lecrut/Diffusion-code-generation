class LinkedListNode:

    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

class MaxFinder:

    def find_maximum(self, head):
        if not head:
            return None
        max_value = head.value
        current = head.next_node
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next_node
        return max_value
if __name__ == '__main__':
    finder = MaxFinder()
    sample_head = LinkedListNode(10, LinkedListNode(5, LinkedListNode(22, LinkedListNode(8, LinkedListNode(30)))))
    result = finder.find_maximum(sample_head)
    print(result)