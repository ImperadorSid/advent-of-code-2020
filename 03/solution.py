# Toboggan Trajectory
import functools

def calc_trees(x, y):
  tree_count = 0
  pos_x = 0
  
  for row in file_array[::y]:
    if row[pos_x % grid_width] == '#':
      tree_count += 1

    pos_x += x

  return tree_count

with open('input.txt', 'r') as input_file:
  file_array = input_file.read().split('\n')

grid_width = len(file_array[0])

print('grid width', grid_width)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = functools.reduce(
  lambda total, factor: total * factor,
  [calc_trees(x, y) for (x, y) in slopes],
)

print(result)
