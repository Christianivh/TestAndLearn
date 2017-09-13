

print("Creacion de una lista de dias de la semana")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]


print("Recorrer la lista mediante un for each in")
for dia in dias:
    print("El dia de la semana %s" % dia )


print("Recorrer la lista mediante un for each in, con enumerate")
for n, dia in enumerate(dias):
    print("El %s dias de la semana %s" % (n, dia) )

print("Recorriendo con while ")
i = 0
while (i < len(dias) ):
      print("El %d dias de la semana %s" % (i, dias[i]) )
      i = i+1;

