class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = {}
        self.salary={}
   
    def add_edge(self, vertex_data, weight):
        self.edges[vertex_data] = weight

    def add_salary(self, vertex_data, salary):
        self.salary[vertex_data] = salary    
    
    def retrieve_edges(self):
        return list(self.edges.keys())

    def retrieve_salary(self):
        return list(self.salary.keys())    

class Graph:
    def __init__(self, directed):
        self.vertices = {}
        self.directed = directed

   
    def add_vertex(self, vertex):
        self.vertices[vertex.data] = vertex

    def add_edge(self, vertex_a, vertex_b, weight):
        self.vertices[vertex_a.data].add_edge(vertex_b.data, weight)
        if not self.directed:
            self.vertices[vertex_b.data].add_edge(vertex_a.data, weight)
    def add_salary(self,vertex_a, vertex_b,salary): 
      self.vertices[vertex_a.data].add_salary(vertex_b.data, salary)
      if not self.directed:
            self.vertices[vertex_b.data].add_salary(vertex_a.data, salary)

    



    def path_exists(self, vertex_a, vertex_b):
     
        to_visit = [vertex_a]
        
        visited = []
        while len(to_visit) > 0:
         
            current = to_visit.pop(0)
            
            visited.append(current)
            if current == vertex_b:
                return True
            else:
               
                vertices = self.vertices[current].edges.keys()
                vertices = self.vertices[current].salary.keys()
                to_visit += [vertex for vertex in vertices if vertex not in visited]
        return False


travel = Graph(directed=False)
Kuwait = Vertex("Kuwait")
Dubai = Vertex("Dubai")
Colombo = Vertex("Colombo")
Male=Vertex("Male")
Riyadh = Vertex("Riyadh")
Tokyo=Vertex("Tokyo")
Oslo=Vertex("Oslo")
travel.add_vertex(Kuwait)
travel.add_vertex(Dubai)
travel.add_vertex(Colombo)
travel.add_vertex(Male)
travel.add_vertex(Riyadh)
travel.add_vertex(Tokyo)
travel.add_vertex(Oslo)
travel.add_edge(Kuwait, Dubai, 2)
travel.add_salary(Kuwait, Dubai, 160)

travel.add_edge(Kuwait, Colombo, 4)
travel.add_salary(Kuwait, Colombo, 200)

travel.add_edge(Colombo,Male , 1)
travel.add_salary( Colombo, Male ,60)

travel.add_edge(Dubai,Riyadh , 1.5)
travel.add_salary( Dubai,Riyadh ,100)

travel.add_edge(Riyadh,Tokyo, 11)
travel.add_salary( Riyadh,Tokyo,500)

travel.add_edge(Dubai,Oslo , 6)
travel.add_salary( Dubai,Oslo ,300)



for city in travel.vertices.keys():
  print(f"-{city}")



f=input("From: ")
t=input("To: ")

if travel.path_exists(f ,t):
 print(f"Time: {travel.vertices[f].edges[t]} Salary:{travel.vertices[f].salary[t]} ")
else:
  print("There is no flights") 
# print(travel.vertices.retrieve_salary())

