# DSatur Algorithm

class dsaturalgo:

    # List of all the available colors(Red, Green, Blue, Yellow, Orange, Purple)
    colors = {}
    # List called cosv which is the Color of that Specific Vertex
    cosv = {}
    # Here, N is Neighbors, empty dictionary for storing neighbors for each vertex.
    N = {}
    # V are the Vertices, here we are creating an empty list to store all of vertex data.
    V = []
    # The Degree of each vertex
    dsaturalgo = {}



    # The choose() function chooses one of the available colors for the Vertex.
    def choose(self):
        u = -1
        i = 0
        while i < len(self.V):
            if self.colors[self.V[i]]:
            # if u is not set then store first vertex (ith) in u
                if u == -1:
                    u = self.V[i]
                # if degree in ith vertex is greater than u then set u as ith vertex
                elif self.dsaturalgo[self.V[i]] > self.dsaturalgo[u]:
                    u = self.V[i]
                # if degree of uth vertex and ith vertex are the same then compare the no of neighbors
                elif self.dsaturalgo[self.V[i]] == self.dsaturalgo[u] and len(self.N[self.V[i]]) > len(self.N[u]):
                    u = self.V[i]
            i += 1
        return u



    # Function to add edge between two vertices which takes two parameters a and b and adds an edge from vertex a to vertex b.
    def AddEdges(self, a, b):
        # Add a to list of vertices if it does not already exist
        if not a in self.V:
            self.CreateVertices(a)
        # Add b to list of vertices if it does not already exist
        if not b in self.V:
            self.CreateVertices(b)
        # Add a and b as each others neighbors
        self.N[a] += [b]
        self.N[b] += [a]

    
    # Function for Creation of Vertices which takes one parameter v as input and adds it to the list of vertices on self and  there will be one more vertex added to self everytime the function is called
    # After adding v , it sets N[v] = [] because no edge has been created yet between these two vertices.
    def CreateVertices(self, v):
        self.V += [v]                   # add new vertex v to list of vertices V
        self.N[v] = []                  # initialize list of neighbors for vertex v
        self.dsaturalgo[v] = 0          # set degree of vertex v as 0 as it doesn't have any neighbors
        self.cosv[v] = None             # set connections of vertex v as none as it doesn't have any connections
    

    
    # We start by iterating through all of the vertices in V(self.V), and setting their available colors property to true then it loops while True, it will continue looping until there are no more vertices left 
    def dsaturalgorithm(self):
        element = 0
        # initialize availability colors in list of colors as true
        while element < len(self.V):
            self.colors[self.V[element]] = True
            element += 1

        while True in self.colors.values():
            # This assigns u with whatever vertex was chosen last time from within the loop
            # when chosen the color is set as unavailable or false
            u = self.choose()
            print('Vertex Selected:', u)
            self.colors[u] = False

            # List of the available colors (R,G,B,Y,O,P)
            available_colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']

            # iterates through all neighbors of the current node, and increases their saturation by one if they are in an available color.
            neighbor = 0
            while neighbor < len(self.N[u]):
            # increase degree of saturation of neighbor by 1
                self.dsaturalgo[self.N[u][neighbor]] += 1          
                # checks to see if any colors have been removed from the list, and removes them if so
                if self.cosv[self.N[u][neighbor]] in available_colors:
                    available_colors.remove(self.cosv[self.N[u][neighbor]])
                    # Print the Name of the connected Vertex and Print the Color of that Vertex
                    print('Neighbor:', self.N[u][neighbor],
                          '& Color of this Vertex:', self.cosv[self.N[u][neighbor]])
                neighbor += 1

            # Colors available currently
            print('Colors Available:', available_colors)
            self.cosv[u] = available_colors[0]

            # Print the color assigned to the Vertex
            print(u, ':', self.cosv[u])
            print()

    # Let the class initialize the object's attributes
    def __init__(self):

        # Input File
        print('DSatur Algorithm')
        file = open('input.txt', 'r')
        print('Opening Input File(input.txt)...')
        for line in file:
            line = line.replace(' ', '').replace('\n', '')
            a, b = line.split(',')
            self.AddEdges(a, b)
        file.close()

        # Calculate DSatur Algo
        self.dsaturalgorithm()

        self.print_out()

        # Displaying the assigned colors
        print('List of all the Vertices and the assigned Color...')

        item = 0
        while(item < len(self.cosv.items())):
            print(list(self.cosv.items())[item][0] + ':', list(self.cosv.items())[item][1])
            item += 1

        file.close()

    def print_out(self):
        print()
        for i in self.V:

            # print the Vertex name
            print('Vertex:', i)

            # print the name of Vertices connected to the selected Vertex
            print('Neighbor:', self.N[i])

            # print the degree of saturation of the vertex
            print('Degree of Saturation:', self.dsaturalgo[i])

            # print the number of Vertices connected to the selected Vertex
            print('Degree of Vertex:', len(self.N[i]))

            print()

dsaturalgo()