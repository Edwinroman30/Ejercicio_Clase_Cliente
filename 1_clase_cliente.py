#Definir una clase Cliente que almacene un código de cliente, cedula, nombre, direccion y fecha Nacimiento.

# En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen 
# suspendidas sus cuentas de ahorro.


#Imprimir por pantalla todos los datos de clientes y el estado que se encuentra
# su cuenta de ahorro.

todos_clientes = []

class Cliente:
    
    def __init__(self,cod_cliente,ced_cliente,nom_cliente,dire_cliente,fech_cliente,estado_cuenta):
        self.cod_cliente = cod_cliente
        self.ced_cliente = ced_cliente
        self.nom_cliente = nom_cliente
        self.dire_cliente = dire_cliente
        self.fech_cliente = fech_cliente
        
        self.cuenta_ahorros = [(estado_cuenta)]
        
        
        self.balance = 0
        self.Datos_cuenta()
        self.cuenta_ahorros.insert(3,[])
        
    #PRUEBAS    
        #Entradas o Ingresos PRODUCIDOS
        #self.Entradas_cuenta('Para mi cumple recibí un regalo', 200)
        #self.Entradas_cuenta('Me encontré 200 en la calle', 200)
        
        #Gastos PRODUCIDOS:
        #self.Gastos_cuenta('Compré un chimi', 50)
        #self.Gastos_cuenta('Recargar el metro', 70)
        
        #self.Mostras_cuenEstado()
    #PRUEBAS     
        
        
     #METODO PARA LA ENTRADAS
    def Entradas_cuenta(self,concepto,valor):
        self.balance = self.balance + valor
        self.cuenta_ahorros[3].append([concepto,valor])
       
        
     #METODO PARA LOS GASTOS
    def Gastos_cuenta(self,concepto,valor):
        self.balance = self.balance - valor
        self.cuenta_ahorros[3].append([concepto,valor])
    

    #INGRESA INFORMACION A LA CUENTA
    def Datos_cuenta(self):
        print('\nBienvenido/a ',self.nom_cliente,'.....')
        self.cuenta_ahorros.append(input('Dígite el código de cuenta (debe de ser de 4 dígitos): '))
        self.cuenta_ahorros.append(input('Entidad Financiera de la cuenta: '))
        self.balance = (float(input('Ingrese su saldo actual: ')))
    
    
    def Determ_estadocuenta(self):
        if(self.cuenta_ahorros[0]):
           return True
        else:
            return False
     
    def Mostras_cuenEstado(self):
        if(self.cuenta_ahorros[0]):
            print('\n{0}, su cuenta de ahorro esta ACTIVADA'.format(self.nom_cliente))
        else:
            print('\n{0}, su cuenta de ahorro esta DESACTIVADA'.format(self.nom_cliente))
            
        print('Su codigo de ahorro es: {0} \nEntidad: {1}'.format(self.cuenta_ahorros[1],self.cuenta_ahorros[2]))
        print('Transacciones realizadas:  \n {}'.format(self.cuenta_ahorros[3]))
        print('Saldo o balance actual es: {}'.format(self.balance))
       
       
       
#FACE FINAL INSTANCIANDO OBJETOS       

todos_clientes.append(Cliente('001','402-122323-2','Pedro Brand','STD Este','10-2-1992',False))
todos_clientes.append(Cliente('002','402-124443-2','Juan Jimenez','Santiao','10-2-1982',True))
todos_clientes.append(Cliente('003','002-122323-2','Laura Garcias','La vega','20-4-1999',True))
todos_clientes.append(Cliente('004','001-144523-5','Elizabeth Jerez','Santiago','10-5-2000',False))

todos_clientes[0].Gastos_cuenta('Compré un chimi', 50)
todos_clientes[3].Entradas_cuenta('Para mi cumple recibí un regalo', 200)


for clientes_inactivos in todos_clientes:
    
    if(clientes_inactivos.Determ_estadocuenta() == False):
        clientes_inactivos.Mostras_cuenEstado()

# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233