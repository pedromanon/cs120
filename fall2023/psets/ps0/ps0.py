#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v.left == None and v.right == None:
        v.size = 1
        return 1
    left = 0
    right = 0
    if v.left:
        left = calculate_sizes(v.left)
    if v.right:
        right = calculate_sizes(v.right)
    v.size = 1 + left + right
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    left = False
    right = False
    leftval = 0
    rightval = 0
    if r.left:
        leftval = r.left.size
        if r.left.size <= r.size/2:
            left = True
    else:
        left = True
    if r.right:
        rightval = r.right.size
        if r.right.size <= r.size/2:
            right = True
    else:
        right = True
    if left and right:
        return r
    else:
        if leftval >= rightval:
            return find_vertex(r.left)
        else:
            return find_vertex(r.right)
