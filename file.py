class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node
    
    def insert_at_position(self,data,position):
        new_node = Node(data)
        if position < 0:
            print("La position doit être un entier positif.")
            return

        if position == 0: 
            self.insert_at_beginning(data)
            return
        
        current = self.head
        index = 0
        prev = None

        while current and index < position:
            prev = current
            current = current.next_node
            index += 1

        if index == position:  
            new_node.next_node = current
            if prev:
                prev.next_node = new_node
        else:
            print("La position est hors de la portée de la liste.")

    def suprimer(self,data):
        current = self.head
        prev = None

        if not current:
            print("la liste est vide !")
            return
        
        if current.data == data:
            self.head = current.next_node
            return
        
        while current:
            if current.data == data:
                prev.next_node = current.next_node
                return
            prev = current
            current = current.next_node
        print(f"L'élément '{data}' n'existe pas dans la liste.")

    def inverse_liste(self):
        current = self.head
        while current:
            ll1.insert_at_beginning(current.data)
            current = current.next_node


    def display(self):
        current = self.head
        while current:
            print(current.data, end = " --> ")
            current = current.next_node
        print("None")

ll = LinkedList()
ll1 = LinkedList()


print("la liste : ",end=""),ll.display()
while True:
    print("======================================================")
    print("saisi d'apré le menu (1/2/3/4/5) :")
    print("1) ajouter au débu de la liste.")
    print("2) ajouter un element dans une place prisis.")
    print("3) suprimer un element.")
    print("4) inverser la liste")
    print("5) quit.")
    try:
        choix = int(input("saisi votre choix : "))
    except:
        print("saisi une valeure numirique !!")
        quit()

    if choix == 1 :
        X = input("saisi l'element a ajouter a debut da la liste : ")
        ll.insert_at_beginning(X)
        print("======================================================")
        print("la liste : ",end=""),ll.display()


    elif choix == 2 : 
        try:
            Y = int(input("saisi la position : "))
        except:
            print("choisi une valeure numirique !!")
            quit()
        X = input("saisi l'element a ajouter dans cette position : ")
        ll.insert_at_position(X,Y)
        print("======================================================")
        print("la liste : ",end=""),ll.display()
        
    elif choix == 3:
        X = input("saisi l'element a supprimer : ")
        ll.suprimer(X)
        print("======================================================")
        print("la liste : ",end=""),ll.display()

    elif choix == 4 :
        ll.inverse_liste()
        ll = ll1
        print("======================================================")
        print("la liste : ",end=""),ll1.display()

    elif choix == 5 :
        quit()

    else:
        print("votre choix n'exeste pas!!")
    