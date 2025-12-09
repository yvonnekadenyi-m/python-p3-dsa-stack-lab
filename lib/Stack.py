
class Stack:

    def __init__(self, items=None, limit=None):
        # optional list
        if items is None:
            self.items = []
        else:
            self.items = items

        self.limit = limit  # maximum stack size

    def push(self, value):
        # Only append if stack is not full
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(value)
        # Else do nothing (ignore push)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    # Tests expect isEmpty()
    def isEmpty(self):
        return len(self.items) == 0

    # Alias
    def empty(self):
        return self.isEmpty()

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        if value not in self.items:
            return -1
        index = self.items.index(value)
        return len(self.items) - 1 - index