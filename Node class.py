# Define your Node class below:
class Node:
    def __init__(self, value, next_node = None):
        print("__init__")
        self.value=value
        self.next_node= next_node

    def get_value(self):
        print("get_value")
        return self.value # takes in pointer(self) returns value (value stored in node) ?

    def get_next_node(self):
        print("get_next_node")
        return self.next_node

    def set_next_node(self, next_node):
        print("set_next_node")
        self.next_node = next_node

node1 = Node("44")
node2 = Node(45)
node3 = Node(46)
print("end of node assignment")

node1.next_node = node2 # node1 -> node2, "44" -> "45"
node2.next_node = node3 # node2 -> node3, "45" -> "46"

print(node1.get_value())