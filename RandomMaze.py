
import random
6
class Cell:
    def __init__(self):
      self.up = True
      self.down = True
      self.right = True
      self.left = True
      self.visited = False

class Maze:
  def __init__(self, width=50, height=50, cell_width=50):
    self.width = width
    self.height = height
    self.cell_width = cell_width
    #Creates an grid of Cell objects for the specific range of the maze
    self.cells = [[Cell() for i in range(height)] for j in range(width)]

  def generate(self):
    x, y = random.choice(range(self.width)), random.choice(range(self.height))
    self.cells[x][y].visited = True
    path = [(x,y)]

    while not all(all(c.visited for c in cell) for cell in self.cells):
      x,y = path[len(path)-1][0], path[len(path)-1][1]

      valid_neighbors = []

      if (self.exists(x,y-1) and not self.cells[x][y-1].visited):
        valid_neighbors.append('up')
      if (self.exists(x,y+1) and not self.cells[x][y+1].visited):
        valid_neighbors.append('down')
      if (self.exists(x+1, y) and not self.cells[x+1][y].visited):
        valid_neighbors.append('right')
      if (self.exists(x-1, y) and not self.cells[x-1][y].visited):
        valid_neighbors.append('left')

      if valid_neighbors:
        next_cell = random.choice(valid_neighbors)
        if next_cell == 'up':
          self.cells[x][y].up = False
          self.cells[x][y-1].down = False
          self.cells[x][y-1].visited = True
          path.append((x, y-1))
        if next_cell == 'down':
            self.cells[x][y].down = False
            self.cells[x][y+1].up = False
            self.cells[x][y+1].visited = True
            path.append((x, y+1))
        if next_cell == 'right':
          self.cells[x][y].right = False
          self.cells[x+1][y].left = False
          self.cells[x+1][y].visited = True
          path.append((x+1, y))
        if next_cell == 'left':
          self.cells[x][y].left = False
          self.cells[x-1][y].right = False
          self.cells[x-1][y].visited = True
          path.append((x-1, y))
      else:
        print(path)
        path.pop()

  def exists(self,x,y):
    if (x < 0 or x > self.width -1 or y < 0 or y > self.height -1):
      return False
    return True
        
  def get_direction(self, direction, x, y):
    if (direction == 'up'):
      return x, y-1
    if (direction == 'down'):
      return x, y+1
    if (direction == 'right'):
      return x+ 1, y
    if (direction == 'left'):
      return x-1, y


if __name__ == '__main__':
    maze = Maze()
    maze.generate()


         
