print("programa para calcular  promedio de calificaciones del alumno")

nombre=raw_input("Ingrese su nombre: ")

num_cali=input("Ingrese numero de calificaciones")

cali_total=0

for i in range(1,num_cali+1):
    print ("ingrese la calificacion numero" + str(i) )
    cali= input()
    cali_total=cali_total + cali
	
promedio=cali_total/num_cali	
print ("El alumno " + str(nombre) +" tiene " + str(num_cali) +"calificaiones "+ "y su promedio es " + str(promedio) )	
