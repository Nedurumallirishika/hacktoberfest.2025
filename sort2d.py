# Sort each row of a 2D array
arr = [
    [5, 2, 9],
    [1, 6, 3],
    [8, 7, 4]
]

print("Original 2D array:")
for row in arr:
    print(row)

# Sorting each row
for row in arr:
    row.sort()

print("\nSorted 2D array (row-wise):")
for row in arr:
    print(row)
