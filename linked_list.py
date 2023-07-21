class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class UnorderedList:
    '''
        Source:
            Methods is_empty, add, size, search and remove are taken from https://bradfieldcs.com/algos/lists/introduction/.
            The other methods are implemented by me. 
    '''

    def __init__(self):
        self.head = None
    
    def print_list(self):
        current = self.head
        l = []
        while current:
            l.append(current.val)
            current = current.next
        print(l)
    
    def is_empty(self):
        return self.head is None
    
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        if self.head:
            current = self.head
        else:
            return 0
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def search(self, item):
        current = self.head
        while current.next is not None:
            if item == current.val:
                return True
            current = current.next
        return False
    
    def remove(self, item):
        current = self.head
        previous = None

        while True:
            if current.val == item:
                break
            previous, current = current, current.next
        
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        '''
            Adds a new item to the end of the list making it the last item in the collection. 
            It needs the item and returns nothing. 
            Assume the item is not already in the list.
        '''
        temp = Node(item)
        current = self.head
        while current.next:
            current = current.next
        if current.next is None:
            current.next = temp

    def insert(self, item, pos):
        '''
            Adds a new item to the list at position pos. 
            It needs the item and returns nothing. 
            Assume the item is not already in the list 
            and there are enough existing items to have position pos.
        '''
        temp = Node(item)
        current = self.head
        current_pos = 0
        try:
            while current_pos < pos - 1:
                current = current.next
                current_pos += 1
        except Exception as e:
            raise e
        next_node = current.next
        current.next = temp
        temp.next = next_node
    
    def pop(self, pos=None):
        '''
            If pos = None: 
                Removes and returns the last item in the list.
                It needs nothing and returns an item.
                Assume the list has at least one item.
            If pos = int:
                Removes and returns the item at position pos. 
                It needs the position and returns the item. 
                Assume the item is in the list.

        '''
        current = self.head
        previous = None
        current_pos = 0
        if type(pos) != int:
            raise Exception('pos must be an integer.')
        if pos is None:
            while current.next:
                previous, current = current, current.next
            previous.next = None
        else:
            while current_pos < pos:
                previous, current = current, current.next
                current_pos += 1
            previous.next = current.next
        return current.val

