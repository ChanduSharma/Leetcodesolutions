class Node:

    def __init__(self, val=0, next_p = None):
        self.val = val
        self.next_p = next_p

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_beg(self, val):

        temp = Node(val=val)
        temp.next_p = self.head
        self.head = temp

    def display(self, node_pointer):

        while node_pointer:
            print(node_pointer.val)
            node_pointer = node_pointer.next_p
    
    def check_palindrome(self):

        if not self.head or not self.head.next_p:
            return True
        
        slw = fast = self.head

        while slw and fast and fast.next_p:
            slw = slw.next_p
            fast = fast.next_p.next_p
        
        cur = slw.next_p if fast else slw
        print("cur")
        self.display(cur)
        temp = None
        while cur:
            nextp = cur.next_p
            cur.next_p = temp
            temp = cur
            cur = nextp
        print("temp")
        self.display(temp)

if __name__ == "__main__":

    l = LinkedList()
    l.insert_at_beg(4)
    l.insert_at_beg(3)
    l.insert_at_beg(2)
    l.insert_at_beg(3)
    l.insert_at_beg(4)
    l.display(l.head)
    l.check_palindrome()