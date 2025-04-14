# Sets and frozenset

# Set
# A set is an unordered, mutable (changable) collection of unique items.
# Defined using curly braces {} or the set () function

# Creating a set
my_set = {1, 2, 3, 4, 5, 4, 3}
print(my_set)

# Adding and removing items
my_set.add(5)
my_set.remove(2)
print(my_set)

# Access items in Sets
my_set = {10, 20, 40, 50}

# Accessing items using a loop
for item in my_set:
    print(item)

# FrozenSets   
# A frozenset is a special type of set in Python that is immutable - once created, you cannot add, remove, or change its elements
# It's just like a regular set (which only stores unique values), but it's frozen- meaning it cannot be modified after creation. 

# Using frozenset() function
numbers = [1, 2, 3, 5, 2, 1]
frozen = frozenset(numbers)
print(frozen) 

a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4 , 5, 6])

# Intersection (common elements)
print(a & b)

# Union (all unique elements)
print(a | b)

# Diference (elements in 'a' not in 'b')
print(a - b)
