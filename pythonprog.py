# String functions
my_string = "Hello, World!"

print("Original String:", my_string)

# 1. upper() - Convert to uppercase
print("Uppercase:", my_string.upper())

# 2. lower() - Convert to lowercase
print("Lowercase:", my_string.lower())

# 3. replace() - Replace a substring
print("Replace 'World' with 'Python':", my_string.replace("World", "Python"))

# 4. split() - Split string into a list
print("Split by comma:", my_string.split(","))

# 5. find() - Find the index of a substring
print("Index of 'World':", my_string.find("World"))


# List functions
my_list = [10, 20, 30, 40, 50]

print("\nOriginal List:", my_list)

# 1. append() - Add item to the end
my_list.append(60)
print("After append(60):", my_list)

# 2. insert() - Insert at specific index
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# 3. pop() - Remove and return item at index
popped_item = my_list.pop()
print("Popped item:", popped_item)
print("After pop():", my_list)

# 4. remove() - Remove specific value
my_list.remove(25)
print("After remove(25):", my_list)

# 5. reverse() - Reverse the list
my_list.reverse()
print("After reverse():", my_list)
