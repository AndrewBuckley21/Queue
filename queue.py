# LAB11.py


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        self.next = new_next

    def __str__(self):
        return "{}".format(self.value)

    __repr__ = __str__


class Queue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
        return self.count

    def enqueue(self, item):
        newNode = Node(item)
        if self.count == 0:
            self.head = newNode
            self.tail = self.head
        elif self.count == 1:
            self.tail = newNode
            self.head.next = self.tail
        else:
            current = self.head
            for i in range(self.count - 1):
                current = current.next
            current.next = newNode
            self.tail = newNode
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return "Queue is empty"
        elif self.count == 1:
            self.count -= 1
            removed = self.head.value
            self.head = None
            return removed
        elif self.count == 2:
            self.count -= 1
            removed = self.head.value
            self.head, self.tail = self.tail, None
            return removed
        else:
            self.count -= 1
            removed = self.head.value
            newHead = self.head.next
            del self.head
            self.head = newHead
            return removed

    def printQueue(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print()

# Collaboration Statement:
# I worked on the homework(lab) assignment alone, using only previous and current course materials.
