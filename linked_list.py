from abstract.data_structure import DataStructure
from node import Node

class LinkedList(DataStructure):
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node()
        node.val = val
        node.next = self.head

        if self.head:
            self.head.prev = node
        
        self.head = node
    
    # TODO: Deleting last node doesn't work
    def delete(self, val):
        if not self.head:
            return None

        curr_node = self.head
        if curr_node and curr_node.val == val:
            self.head = curr_node.next
            return curr_node

        while curr_node.val != val:
            curr_node = curr_node.next
        
        prev = curr_node.prev

        if prev and curr_node.next:
            prev.next = curr_node.next
            curr_node.next.prev = prev

        return curr_node

    def print_all(self):
        curr_node = self.head
        while curr_node != None:
            print curr_node.val
            curr_node = curr_node.next
    
    def find(self):
        # return Node or None
        pass