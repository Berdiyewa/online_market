from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random, os
from tkinter import messagebox
from time import strftime



class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x1000+0+0')
        self.root.title("SuperMarket")
        self.root.config(bg='orange')

        global count
        self.name_cust = StringVar()
        self.bill = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.item = IntVar()
        self.sub_totalv = StringVar()
        self.tax = StringVar()
        self.totalv = StringVar()
        z = random.randint(1000, 9999)
        self.bill.set(z)



        self.categories = ["dairy", "meat", "beverages"]

        self.scateg_diary = ["Milk", "Butter", "Yogurt", "Cheese"]
        self.milk = ["Home", "Dere", "Elin"]
        self.price_home = 12
        self.price_dere = 20
        self.price_elin = 18

        self.butter = ["elin", "taze ay"]
        self.price_but_elin = 30
        self.price_but_taze_ay = 25
        self.yogurt = ["alpenald", "elin_yogurt"]
        self.price_alpenald = 5
        self.price_elin_yog = 6

        self.cheese = ["taze ay", "halal", "home"]
        self.price_cheese_taze = 15
        self.price_halal = 18
        self.price_cheese_home = 18

        self.scateg_meat = ["Cow meat", "Chicken meat", "Sheep meat"]
        self.cow_meat = ["boneless meat", "meat bone"]
        self.price_boneless = 70
        self.price_bone = 35

        self.cow_meat = ["whole chicken", "chicken legs", "chicken wings"]
        self.price_whole = 30
        self.price_legs = 20
        self.price_wings = 15

        self.sheep_meat = ["boneless meat", "meat bone"]
        self.price_sheep_boneless = 50
        self.price_sheep_bone = 15

        self.scateg_beverages = ["Water", "Carbonated drinks", "Juice"]
        self.water = ["archalyk"]
        self.price_archa = 5

        self.carbonate = ["bold", "archalyk"]
        self.price_bold = 6
        self.price_archalyk = 5

        self.jucie = ["saba", "7gen", "pokgije"]
        self.price_saba = 18
        self.price_7gen = 17
        self.price_pokgije = 5

        
        

        # ========= upper images ============

        img1 = Image.open('image/gok.jpeg')
        img1 = img1.resize((300,200), Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1, bg='orange')
        lbl_img1.place(x=0, y=0, width=300, height=200)

        img2 = Image.open('image/market.jpeg')
        img2 = img2.resize((300,200), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bg='orange')
        lbl_img2.place(x=300, y=0, width=300, height=200)

        img3 = Image.open('image/gok.jpeg')
        img3 = img3.resize((300,200), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root, image=self.photoimg3, bg='orange')
        lbl_img3.place(x=600, y=0, width=300, height=200)

        img4 = Image.open('image/market.jpeg')
        img4 = img4.resize((300,200), Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl_img4 = Label(self.root, image=self.photoimg4, bg='orange')
        lbl_img4.place(x=900, y=0, width=300, height=200)

        # ========= title + frame ============

        lbl_title = Label(self.root, text='Super Market Registration Form', font=('Times', 20, 'bold'), 
                     fg='white', bg='green', bd=10, relief=GROOVE) 
        lbl_title.place(x=0, y=200, width=1200, height=60)

        main_frame = Frame(self.root, bg='orange', bd=6, relief=GROOVE)
        main_frame.place(x=0, y=260, width=1200, height=740)

        # ========= upper images ============

        customer_frame = LabelFrame(main_frame, text='Customer:', font=('Times', 14, 'bold'), 
                                    fg='green', bg='white')
        customer_frame.place(x=10, y=0, width=300, height=160)

        # =====================
        self.bill_lbl = Label(customer_frame, text='Bill No:', font=('Arial', 12, 'bold'),
                                fg='green', bg='white', justify=CENTER)
        self.bill_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.bill_entry = Entry(customer_frame, font=('Times', 12), width=15, textvariable=self.bill)
        self.bill_entry.grid(row=1, column=1, padx=10)

        self.name_cust_lbl = Label(customer_frame, text='Customer name:', font=('Arial', 12, 'bold'),
                                   fg='green', bg='white', justify=CENTER)
        self.name_cust_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.name_cust_entry = Entry(customer_frame, font=('Times', 12), width=15, textvariable=self.name_cust)
        self.name_cust_entry.grid(row=0, column=1, padx=10)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(customer_frame, font=("Times", 14, 'bold'))
        lbl.place(x=50, y=100, width=130, height=20)
        time()

        # ========== counter_frame ===========

        counter_frame = LabelFrame(main_frame, text='Bill Counter:', font=('Times', 14, 'bold'), fg='green', bg='white')
        counter_frame.place(x=320, y=0, width=300, height=160)

        # =====================
        self.sub_total_lbl = Label(counter_frame, text='Sub Total:', font=('Arial', 12, 'bold'),
                                   fg='green', bg='white', justify=CENTER, width=10)
        self.sub_total_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.sub_total_entry = Entry(counter_frame, font=('Times', 12), width=17)
        self.sub_total_entry.grid(row=0, column=1, padx=10)

        self.tax_lbl = Label(counter_frame, text='Tax:', font=('Arial', 12, 'bold'),
                             fg='green', bg='white', justify=CENTER, width=10)
        self.tax_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.tax_entry = Entry(counter_frame, font=('Times', 12), width=17)
        self.tax_entry.grid(row=1, column=1, padx=10)

        self.total_lbl = Label(counter_frame, text='Total:', font=('Arial', 12, 'bold'),
                               fg='green', bg='white', justify=CENTER, width=10)
        self.total_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.total_entry = Entry(counter_frame, font=('Times', 12), width=17)
        self.total_entry.grid(row=2, column=1, padx=10)

        # ========== product_frame ===========

        product_frame = LabelFrame(main_frame, text='Product', font=('Times', 14, 'bold'), 
                                   fg='green', bg='white')
        product_frame.place(x=630, y=0, width=550, height=670)


        self.category_lbl = Label(product_frame, text='Select Category:', font=('Arial', 12),
                                  fg='green', bg='white')
        self.category_lbl.grid(row=0, column=0, pady=6)

        self.combo_category = ttk.Combobox(product_frame, values=self.categories, state='readonly', font=('Times', 12), foreground='saddlebrown', background='white')
        self.combo_category.current(0)
        self.combo_category.grid(row=0, column=1)
        self.combo_category.bind("<<ComboboxSelected>>", self.categories)

        self.sub_category_lbl = Label(product_frame, text='Subcategory:', font=('Arial', 12),
                                      fg='green', bg='white')
        self.sub_category_lbl.grid(row=1, column=0, pady=6)

        self.combo_sub_categ = ttk.Combobox(product_frame, font=('Times', 12), values=[""], state='readonly', foreground='saddlebrown', background='white')
        self.combo_sub_categ.current()
        self.combo_sub_categ.grid(row=1, column=1)
        self.combo_category.bind("<<ComboboxSelected>>", self.scateg)

        self.product_lbl = Label(product_frame, text='Product Name:', font=('Arial', 12),
                                 fg='green', bg='white')
        self.product_lbl.grid(row=2, column=0, pady=6)

        self.combo_prod = ttk.Combobox(product_frame, font=('Times', 12), textvariable=self.product, foreground='saddlebrown', background='white')
        self.combo_prod.current()
        self.combo_prod.grid(row=2, column=1)
        self.combo_category.bind("<<ComboboxSelected>>", self.price)

        self.price_lbl = Label(product_frame, text='PRICE:', font=('Arial', 12, 'bold'),
                               fg='green', bg='white', width=6)
        self.price_lbl.grid(row=0, column=2)

        self.combo_price = ttk.Combobox(product_frame, font=('Times', 12), textvariable=self.prices, foreground='saddlebrown', background='white', width=12)
        self.combo_price.current()
        self.combo_price.grid(row=0, column=3)

        self.item_lbl = Label(product_frame, text='Item:', font=('Arial', 12, 'bold'),
                               fg='green', bg='white', width=6)
        self.item_lbl.grid(row=1, column=2)

        self.ent_item = Entry(product_frame, font=('Times', 14), textvariable=self.item, foreground='saddlebrown', background='white', width=12)
        self.ent_item.grid(row=1, column=3)

        self.search_lbl = Label(product_frame, text='Search:', font=('Arial', 12, 'bold'),
                                fg='orange', bg='white', justify=CENTER)
        self.search_lbl.grid(row=4, column=0, pady=10)
        self.search_entry = Entry(product_frame, font=('Times', 14), width=22, textvariable=self.search_bill)
        self.search_entry.grid(row=4, column=1, padx=6)
        self.btn_search = Button(product_frame, text='Search', font=('Arial', 12, 'bold'),
                                 fg='orange', bg='white', width=10)
        self.btn_search.grid(row=4, column=3, columnspan=4)


        # +++++++++++ Bill area frame ++++++++++++

        check_frame = LabelFrame(product_frame, text='Check list',font=('Times', 14),  
                                 fg='white', bg='Lightgreen', bd=6, relief=GROOVE)
        check_frame.place(x=0, y=150, width=550, height=400)

        y_scroll = Scrollbar(check_frame, orient=VERTICAL)
        self.inf_text = Text(check_frame, font=('Times', 14, 'bold'), bg='white',
                             fg='green', yscrollcommand=y_scroll.set)
        y_scroll.config(command=self.inf_text.yview)
        y_scroll.pack(side=RIGHT, fill=Y)
        self.inf_text.pack(fill=BOTH, expand= TRUE)

        self.btn_add = Button(product_frame, text='Add to List', command=self.add_list, font=('Arial', 12, 'bold'), fg='orange', bg='white', width=8, height=1)
        self.btn_add.place(x=5, y=570)

        self.btn_gen = Button(product_frame, text='Generate check', font=('Arial', 12, 'bold'), fg='orange', bg='white', width=12, height=1)
        self.btn_gen.place(x=180, y=570)

        self.btn_save = Button(product_frame, text='Save check', command=self.add_to_list, font=('Arial', 12, 'bold'), fg='orange', bg='white', width=8, height=1)
        self.btn_save.place(x=350, y=570)

        self.btn_total = Button(product_frame, text='Total', command=self.sub_total, font=('Arial', 12, 'bold'), fg='orange', bg='white', width=8, height=1)
        self.btn_total.place(x=5, y=610)

        self.btn_clear = Button(product_frame, text='Clear', font=('Arial', 12, 'bold'), fg='orange', bg='white', width=8, height=1)
        self.btn_clear.place(x=180, y=610)

        self.btn_exit = Button(product_frame, text='Exit', command=exit, font=('Arial', 12, 'bold'), fg='orange', bg='white', width=8, height=1)
        self.btn_exit.place(x=350, y=610)
        self.welcome()

        # ========== center images ===========

        center_img_frame = Frame(main_frame, bg='orange')
        center_img_frame.place(x=10, y=167, width=610, height=240)

        img5 = Image.open('image/market.jpeg')
        img5 = img5.resize((300,240), Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl_img5 = Label(center_img_frame, image=self.photoimg5)
        lbl_img5.place(x=0, y=0, width=300, height=240)

        img6 = Image.open('image/gok.jpeg')
        img6 = img6.resize((300,240), Image.BILINEAR)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        lbl_img6 = Label(center_img_frame, image=self.photoimg6)
        lbl_img6.place(x=310, y=0, width=300, height=240)


        # ========== treeview ===========

        treeview_frame = Frame(main_frame, bg='white')
        treeview_frame.place(x=10, y=420, width=610, height=250)

        tree_scroll_x = Scrollbar(treeview_frame, orient=HORIZONTAL)
        tree_scroll_y = Scrollbar(treeview_frame, orient=VERTICAL)

        self.my_tree = ttk.Treeview(treeview_frame, xscrollcommand=tree_scroll_x.set, yscrollcommand=tree_scroll_y, selectmode=EXTENDED)
        self.my_tree['columns'] = ('Customer name', 'Bill No', 'Sub total', 'Tax', 'Total')

        self.my_tree.pack()

        tree_scroll_x.config(command=self.my_tree.xview)
        tree_scroll_y.config(command=self.my_tree.yview)

        tree_scroll_x.pack(side=BOTTOM, fill=X)
        tree_scroll_y.pack(side=RIGHT, fill=Y)

        # +++++++++++ create columns 
        self.my_tree.column('#0', width=0, stretch= NO)         # show='headings'

        self.my_tree.column('Customer name', anchor= CENTER, width=200)
        self.my_tree.column('Bill No', anchor= CENTER, width=100)
        self.my_tree.column('Sub total', anchor= CENTER, width=100)
        self.my_tree.column('Tax', anchor= CENTER, width=100)
        self.my_tree.column('Total', anchor= CENTER, width=100)
        
        # +++++++++++ create heading columns
        self.my_tree.heading('#0', text='', anchor=W)

        self.my_tree.heading('Customer name', anchor= CENTER, text='Customer name')
        self.my_tree.heading('Bill No', anchor= CENTER, text='Bill No')
        self.my_tree.heading('Sub total', anchor= CENTER, text='Sub total')
        self.my_tree.heading('Tax', anchor= CENTER, text='Tax')
        self.my_tree.heading('Total', anchor= CENTER, text='Total')

        self.my_tree.tag_configure('oddrow', background='white')
        self.my_tree.tag_configure('evenrow', background='lightgreen')


        data = [
            ['Berdi Nuryyew', '120899', '1000', '10%', '1010'],
            ['Mahri Nuryyewa', '040101', '1000', '10%', '1010'],
            ['Aylar Nuryyew', '071298', '1000', '10%', '1010'],
            ['Lachyn Ahmedowa', '150797', '1000', '10%', '1010'],
            ['Nury Nuryyew', '030792', '1000', '10%', '1010'],
            ['Berdi Nuryyew', '120899', '1000', '10%', '1010'],
            ['Mahri Nuryyewa', '040101', '1000', '10%', '1010'],
            ['Aylar Nuryyew', '071298', '1000', '10%', '1010'],
            ['Lachyn Ahmedowa', '150797', '1000', '10%', '1010'],
            ['Nury Nuryyew', '030792', '1000', '10%', '1010'],
            ['Berdi Nuryyew', '120899', '1000', '10%', '1010'],
            ['Mahri Nuryyewa', '040101', '1000', '10%', '1010'],
            ['Aylar Nuryyew', '071298', '1000', '10%', '1010'],
            ['Lachyn Ahmedowa', '150797', '1000', '10%', '1010'],
            ['Nury Nuryyew', '030792', '1000', '10%', '1010'],
            ['Berdi Nuryyew', '120899', '1000', '10%', '1010'],
            ['Mahri Nuryyewa', '040101', '1000', '10%', '1010'],
            ['Aylar Nuryyew', '071298', '1000', '10%', '1010'],
            ['Lachyn Ahmedowa', '150797', '1000', '10%', '1010'],
            ['Nury Nuryyew', '030792', '1000', '10%', '1010']
        ]

        count = 0
        for record in data:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow'))
            else:
                self.my_tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow'))
            count += 1
        
        self.list=[]
        '''
        self.n=self.prices.get()
        self.m=self.item.get()*self.n
        self.list.append(self.m)
        if self.product.get()=='':
            messagebox.showerror('Error, Select the product name')
        else:
            self.inf_text.insert(END, "\n {self.product.get()}\t{self.item.get()}\t\t{self.m}")
            self.sub_total_entry.set(str('Rs.%.2f'%(sum(self.list))))
            self.tax_entry.set(str('Rs.%.2f'%((((sum(self.list)) - (self.prices.get()))*Tax)/100)))
            self.total_entry.set(str('Rs.%.2f'%(sum(self.list)) + ((((sum(self.list)) - (self.prices.get()))*Tax)/100)))
        '''
    


    def sub_total(self):
        self.sub_total_entry.delete(0, END)
        if self.combo_price.get() == '18':
            tot1 = f'{int(self.combo_price.get()) * int(self.ent_item.get())}'
            self.sub_total_entry.insert(END, tot1)

    def total(self):
        self.total_entry.delete(0, END)
        tax = self.tax_entry == 20

        tot1 = f'{int(self.tax_entry.get()) * int(tax)}'
        self.total_entry.insert(END, tot1)

    def welcome(self):
        self.inf_text.delete(1.0, END)
        self.inf_text.insert(END, f'\t\t Welcome to market:\n')
        self.inf_text.insert(END, f' Bill Number: {self.bill.get()}\n')
        self.inf_text.insert(END, f' Customer name: {self.name_cust.get()}\n')
        self.inf_text.insert(END, '===========================================')
        self.inf_text.insert(END, f'\n Product name\t\t\tITEM \t         Total price\n')
        self.inf_text.insert(END, '===========================================')

    def add_list(self):
        self.n=self.prices.get()
        self.m=self.item.get()*self.n
        self.list.append(self.m)
        if self.product.get()=='':
            messagebox.showerror('Error', 'Select the product name')
        else:
            self.inf_text.insert(END, f"\n {self.product.get()}\t{self.item.get()}\t\t{self.m}")
            self.sub_total_entry.set(str('Rs.%.2f'%(sum(self.list))))
            self.tax_entry.set(str('Rs.%.2f'%((((sum(self.list)) - (self.prices.get()))*self.tax)/100)))
            self.total_entry.set(str('Rs.%.2f'%(sum(self.list)) + ((((sum(self.list)) - (self.prices.get()))*self.tax)/100)))
            
            self.inf_text.insert(END, f' {self.combo_prod.get()}\t\t\t {self.ent_item.get()}\t\t\t {self.total_entry.get()}')
        
    def add_to_list(self):
        global count
        
        self.my_tree.insert(parent='', index='end', iid=count, text='', values=(self.name_cust_entry.get(), 
                            self.bill_entry.get(), self.sub_total_entry.get(), self.tax_entry.get(), self.total_entry.get()))
        count += 1

    def clear(self):
        self.inf_text.delete(1.0, END)
        self.name_cust.set('')
        x=random.randint(1000, 9999)
        self.bill.set(str(str(x)))
        self.search_bill.set('')
        self.product.set('')
        self.prices.set('')
        self.item.set('')
        self.list=[0]
        self.totalv.set('')
        self.sub_totalv.set('')
        self.tax.set('')
        self.welcome()



    def categories(self, event=""):
            if self.combo_category.get()=="diary":
                self.combo_sub_categ.config(values=self.scateg_diary)
                self.combo_sub_categ.current(0)

            if self.combo_category.get()=="meat":
                self.combo_sub_categ.config(values=self.scateg_meat)
                self.combo_sub_categ.current(0)

            if self.combo_category.get()=="beverages":
                self.combo_sub_categ.config(values=self.scateg_beverages)
                self.combo_sub_categ.current(0)
    
    def scateg(self, event=""):
        if self.combo_sub_categ.get()=="Milk":  
            self.combo_prod.config(values=self.milk)
            self.combo_prod.current(0)
        if self.combo_sub_categ.get()=="Butter":  
            self.combo_prod.config(values=self.butter)
            self.combo_prod.current(0)
        if self.combo_sub_categ.get()=="Yogurt":  
            self.combo_prod.config(values=self.yogurt)
            self.combo_prod.current(0)
        if self.combo_sub_categ.get()=="Cheese":  
            self.combo_prod.config(values=self.cheese)
            self.combo_prod.current(0)
    
    def price(self, event=""):
        if self.combo_prod.get() == "Home":
            self.combo_price.config(values=self.price_home)
            self.combo_price.current(0)
            self.item.set(1)
        if self.combo_prod.get() == "Dere":
            self.combo_price.config(values=self.price_dere)
            self.combo_price.current(0)
            self.item.set(1)
        if self.combo_prod.get() == "Elin":
            self.combo_price.config(values=self.price_elin)
            self.combo_price.current(0)
            self.item.set(1)



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()