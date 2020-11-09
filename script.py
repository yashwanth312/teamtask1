import os
import getpass
import webbrowser as wb
import subprocess

def EC2():
    while True :
      print("Choose from the options provided :  ")
      print()
      print("1 : View Running Instances")
      print("2 : Create a Key Pair")
      print("3 : Create a security group and Configure Created Security Group")
      print("4 : Add Ingress Rules to Security Group")
      print("5 : Launch an instance")
      print("6 : Create an EBS Storage")
      print("7 : Attach an EBS Storage")
      print("8 : Return to Main Menu")
      print("9 : Exit Program")
      ans = input("Enter your choice : ")
      print()
      if ans == "1" :
        os.system("clear")
        os.system('aws ec2 describe-instances')
      elif ans == "2" :
        os.system("clear")
        name = input("Name of Key Pair: ")
        os.system('aws ec2 create-key-pair --key-name {0} --query KeyMaterial --output text > {0}.pem'.format(name))
        print("Key Created Successfully")
      elif ans == "3" :
        os.system("clear")
        name = input("Name of Security Group: ")
        des = input("A little description of your security group: ")
        os.system('aws ec2  create-security-group --group-name {} --description "{}" '.format(name,des))
        print("!! Security Group created Successfully !!")
        print()
        print("Configuring security group......\n")
        print('Example:\n For SSH from any IPv4: \n tcp,22,0.0.0.0/0')
        info = input("Protocol: ,Port No: , CIDR Range: ")
        info = info.split(',')
        os.system('aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}'.format(name,info[0],info[1],info[2]))
        print("!! Security Group Created Successfully")
        print("You can allow more ingress rules from the config menu")
      elif ans == "4" :
        os.system("clear")
        print("Adding Ingress Rules in Security Group........")
        name = input("Name of Security Group: ")
        info = input("Protocol: ,Port No: , CIDR Range: ")
        info = info.split(',')
        os.system('aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}'.format(name,info[0],info[1],info[2]))
        print("!! Ingress Rules Added Successfully")
      elif ans == "5" :
        os.system("clear")
        print("Launch an Instance")
        print()
        print("Example: Redhat AMI = ami-052c08d70def0ac62")
        image = input("AMI ID: ")
        cout = input("No. of Instances: ")
        print()
        print("Example: t2.micro is one the Instance type available free for 12-months from registration")
        instype = input("Instance type: ")
        key = input("Key Name: ")
        sgname = input("Security Group Name:")
        print("Output: ")
        os.system('aws ec2 run-instances --image-id {} --count {}  --instance-type {}  --key-name {} --security-groups {} '.format(image,cout,instype,key,sgname))
        print()
        print("Instance Launch Success")
      elif ans == "6":
        os.system("clear")
        print("Create an EBS Storage......")
        print()
        vol = input("Volume-type (Default gp2) : ")
        size = input("Size (in GBs): ")
        print()
        az = input("Availability Zone: ")
        os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vol,size,az))
      elif ans == "7":
        os.system("clear")
        print("Attach EBS storage to any Instance ......")
        vid = input("Volume ID: ")
        iid = input("Instance ID: ")
        os.system('aws ec2 attach-volume volume-id {} --instance-id {} --device /dev/sdf'.format(vid,iid))
      elif ans == "8" :
        os.system("clear")
        break
      elif ans == "9" :
        os.system("clear")
        exit()

def S3():
    while True :
      print("Choose from the options provided......: ")
      print("1 : View Running S3 Storage")
      print("2 : Create an Object Storage S3")
      print("3 : Delete an S3 Bucket")
      print("4 : Public Access for Buckets")
      print("5 : Put an Object into Bucket")
      print("6 : Manage Object Permissions")
      print("7 : Return to Main Menu")
      print("8 : Exit the program")
      ans = input("Enter your choice : ")
      if ans == "1" :
        os.system("clear")
        os.system('aws s3api list-buckets')
      elif ans == "2" :
        os.system("clear")
        name = input("Name of Bucket: ")
        region = input("Region to which Bucket has to be Launched: ")
        os.system('aws s3api create-bucket --bucket {0} --region {1} --create-bucket-configuration LocationConstraint={1}  --object-lock-enabled-for-bucket '.format(name,region))
        print("!! Bucket Created Successfully !!")
      elif ans == "3" :
        os.system("clear")
        name = input("Name of Bucket: ")
        region = input("Region on which Bukcet is present: ")
        os.system('aws s3api delete-bucket --bucket {} --region {} '.format(name,region))
        print("!! Bucket Created Successfully !!")
      elif ans == "4":
        os.system("clear")
        name = input("Name of Bucket: ")
        choice = input("Public Access Allow(y)/Disable(n): ")
        if choice == "y":
            os.system('aws s3api put-public-access-block --bucket {} --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" '.format(name))
        elif choice == "n":
            os.system('aws s3api put-public-access-block --bucket {} --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true" '.format(name))
      elif ans == "5":
        os.system("clear")
        name = input("Name of Bucket: ")
        path = input("Location/Path of Object in Your OS/PC: ")
        opath = input("Location/Path of Object to be reflected in S3: ")
        os.system('aws s3api put-object --bucket {} --key {} --body {} '.format(name,opath,path))
      elif ans == "6":
        os.system("clear")
        name = input("Nameof Bucket: ")
        opath = input("Location/Path of Object in S3: ")
        print("1: Make Object Public Readable")
        print("2: Make Object Public Read-Writable")
        print("3: Make Object Private")
        ans = input("Your Answer: ")
        if ans == "1":
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl "public-read" '.format(name,opath))
        elif ans == "2":
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl "public-read-write" '.format(name,opath))
        elif ans == "3":
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl "private" '.format(name,opath))
        else:
            print("Unsupported Option")
            exit()
        print("!! Permissions Changed Successfully !!")
      elif ans == "7" :
          os.system("clear")
          break
      elif ans == "8" :
          os.system("clear")
          exit()
      else:
        print("Unsupported Option")

while True :
  print("---------------------Hey there !!!!!--------------------")
  print()
  print("----------Choose from the widest range of options-------")
  print()
  print()
  print("Enter the numbers of your choice")
  print("""        1 : Explore the EC2 services of the amazon cloud
        2 : Explore S3 services
        3 : Enter the docker world 
        4 : Manage bigdata using Hadoop
        5 : LVM (elastic storage)
        6 : Linux commands
        7 : Configure Webserver
        8 : Exit the program""")
 
  choice = input("Enter your choice : ")
  if choice == '3' :
    while True :
      print(""" Press 1 : For installing and starting up with docker
      Press 2 : To start docker if pre-installed
      Press 3 : Main Menu
      Press 4 : Exit Program""")
      ya = input("Enter your choice : ")
      if ya == '1' :
        os.system('echo [docker]>>doc.repo')

        os.system('echo baseurl=http://download.docker.com/linux/centos/7/x86_64/stable>>doc.repo')

        os.system('echo gpgcheck=0>>doc.repo')

        os.system('cp doc.repo  /etc/yum.repos.d')

        os.system('yum install docker-ce --nobest -y')

        os.system('systemctl start docker')
      elif ya == '2' : 
        while True :
          print(""" Choose various services of docker to be managed 
          1 : Containers
          2 : Images
          3 : Volumes
          4 : Networking
          5 : Docker Installation Menu
          6 : Exit Program""")
          ch = input("Enter your choice : ") 
          if ch == '1' :
            while True :
              print(""" Explore the services of containers 
              1 : Create a container
              2 : List of all running containers
              3 : List of all contianers 
              4 : Start  a container
              5 : Stop a container
              6 : Remove container
              7 : Execute any commands inside a container
              8 : Docker Menu
              9 : Exit Program""")
              cont = input("Enter your choice (Container) ")
              if cont == '1' :
                imp=input("Enter image name: ")
                a=input("Enter container name:")
                b=input("Enter the ports to be exposed:")
                c=input("Enter the network name:")
                d=input("Enter the source volume file:")
                e=input("Enter the destination path:")
                if len(a)==0 and len(b)==0 and len(c)==0 and len(d)==0 and len(e)==0 :
                  
                  os.system("clear")
                  os.system("docker run -dit "+ imp)
                elif len(a)==0 and len(b)==0 and len(c)==0 :
                  os.system("clear")
                  os.system("docker run -dit -v " + d +":" + e + " " + imp)
                elif len(b)==0 and len(c)==0 and len(d)==0 and len(e)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name " + a + " " + imp)
                elif len(a)==0 and len(c)==0 and len(d)==0 and len(e)==0 :
                  os.system("clear")
                  os.system("docker run -dit -p " + b + " " + imp)
                elif len(a)==0 and len(b)==0 and len(d)==0 and len(e)==0 :
                  os.system("clear")
                  os.system("docker run -dit --network=" + c + " " + imp)
                elif len(a)==0 and len(b)==0 :
                  os.system("clear")
                  os.system("docker run -dit --network=" + c + " -v " + d + ":" + e + " " + imp)
                elif len(a)==0 and len(c)==0 :
                  os.system("clear")
                  os.system("docker run -dit -p " + b + " -v " + d + ":" + e + " " + imp)
                elif len(a)==0 and len(d)==0 and len(e)==0  :
                  os.system("clear")
                  os.system("docker run -dit -p " + b +" --network=" + c + " " + imp)
                elif len(b)==0 and len(c)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a + " -v " + d + ":" + e + " " + imp)
                elif len(b)==0 and len(d)==0 and len(e)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a + " --network=" + c + " " + imp)
                elif len(c)==0 and len(d)==0 and len(e)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a + " -p " + b + " " + imp)
                elif len(a)==0 :
                  os.system("clear")
                  os.system("docker run -dit -p " + b + " --network=" + c + " -v " + d + ":" + e + " " +  imp)
                elif len(b)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a + " --network=" + c + " -v " + d + ":" + e + " " + imp)
                elif len(c)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a + " -p " + b + " -v " + d + ":" + e + " " + imp)
                elif len(d)==0 and len(e)==0 :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a +" -p " + b + " --network=" + c + " " + imp)
                else :
                  os.system("clear")
                  os.system("docker run -dit --name=" + a + " -p " + b + " --network=" + c + " -v " + d + ":" + e + " " + imp)
              elif cont == '2' :
                os.system("clear")
                os.system("docker ps")
              elif cont == '3' :
                os.system("clear")
                os.system("docker ps -a")
              elif cont == '4' : 
                start = input("Enter the name or ID of the container to be started : ")
                os.system("clear")
                os.system("docker start " + start)
              elif cont == '5' :
                stop = input("Enter the name or ID of the container to be stopped : ")
                os.system("clear")
                os.system("docker stop " + stop)
              elif cont == '6' :
                rm = input("Enter the name or ID of the container to be removed : ")
                os.system("clear")
                os.system("docker rm -f " + rm)
              elif cont == '7' :
                co = input("Enter the name or ID of the container to run a command inside : ")
                ex = input("Enter the command to run : ")
                os.system("clear")
                os.system("docker exec " + co + " " + ex)
              elif cont == '8' :
                os.system("clear")
                break
              elif cont == '9' :
                os.system("clear")
                exit()
              else :
                os.system("clear")
                print("Enter a valid option")
          elif ch == '2' :
            while True :
              print("""Explore the of IMAGES.....
              1 : Download any image
              2 : Inspect an image 
              3 : List all images
              4 : Remove an image
              5 : Docker Menu
              6 : Exit Program""")
              im = input("Enter your choice (Images) : ")
              if im == '1' :
                d = input("Enter the name of the image to be downloaded : ")
                os.system("clear")
                os.system("docker pull " + d)
              elif im == '2' :
                i = input("Enter the name of the image : ")
                os.system("clear")
                os.system("docker image inspect " + i)
              elif im == '3' :
                os.system("clear")
                os.system("docker image ls")
              elif im == '4' :
                rem = input("Enter the name of the image : ")
                os.system("clear")
                os.system("docker image rm " + rem)
              elif im == '5' :
                os.system("clear")
                break
              elif im == '6' : 
                os.system("clear")
                exit()
              else :
                os.system("clear")
                print("Enter a valid option")
          elif ch == '3' :
            while True :
              print("""Explore the services of VOLUMES.....
              1 : Create a volume
              2 : Inspect a volume
              3 : List all volumes
              4 : Remove volume
              5 : Docker Menu
              6 : Exit Program""")
              vol=input("Enter your choice (Volumes) : ")
              if vol == '1' :
                c = input("Enter the name of volume : ")
                os.system("clear")
                os.system("docker volume create " + c)
              elif vol == '2' :
                i = input("Enter the name of volume : ")
                os.system("clear")
                os.system("docker volume inspect " + i)
              elif vol == '3' :
                os.system("clear")
                os.system("docker volume ls")
              elif vol == '4' :
                r = input("Enter the name of volume : ")
                os.system("clear")
                os.system("docker volume rm " + r)
              elif vol == '5' :
                os.system("clear")
                break
              elif vol == '6' :
                  os.system("clear")
                  exit()
              else :
                os.system("clear")
                print("Enter a valid option")
          elif ch == '4' :
            while True :
              print("""Explore the services of NETWORKING.....
              1 : Create a network
              2 : Inspect any network
              3 : List all networks
              4 : Remove any network
              5 : Connect any container to a network
              6 : Disconnect any container from a network
              7 : Docker Menu
              8 : Exit Program""")         
              net = input("Enter your choice (Networking) : ")
              if net == '1' :
                cr = input("Enter the name of network : ")
                os.system("clear")
                os.system("docker network create " + cr)
              elif net == '2' :
                ins = input("Enter the name of network : ")
                os.system("clear")
                os.system("docker network inspect " + ins)

              elif net == '3' :
                os.system("clear")
                os.system("docker network ls")
              elif net == '4' :
                rmn = input("Enter the name of network : ")
                os.system("clear")
                os.system("docker network rm  " + rmn)
              elif net == '5' :
                cot = input("Enter the name of the container : ")
                n1 = input("Enter the name of network : ")
                os.system("clear")
                os.system("docker network connect " + n1 + " " + cot)
              elif net == '6' :
                cotr = input("Enter the name of the container : ")
                n2 =input("Enter the name of network : ")
                os.system("clear")
                os.system("docker network disconnect " + n2 + " " + cotr)
              elif net == '7' :
                os.system("clear")
                break
              elif net == '8' :
                os.system("clear")
                exit()
              else :
                os.system("clear")
                print("Enter a valid option")
          elif ch == '5' :
            os.system("clear")
            break
          elif ch == '6' :
            os.system("clear")
            exit()
      elif ya == '3' :
          os.system("clear")
          break
      elif ya == '4' :
          os.system("clear")
          exit()
      else :
        os.system("clear")
        print("Enter a valid option")
  elif choice == "2" :
    S3() 
  elif choice == "1" :
    EC2()
  elif choice == "5" :
      while True :
        print(""" Choose from the options below ........
        1 : View all the storage devices attached
        2 : Physical Volume (PV)
        3 : Volume Group (VG)
        4 : Logical Volume (LV)
        5 : Return to Main Menu
        6 : Exit Program""")
        st = input("Enter your choice : ")
        if st == "1" :
          os.system("clear")
          os.system("fdisk -l")
        elif st == "2" :
          while True :
            print(""" Choose from options of PV .....
            1 : Create a physical volume
            2 : Info about created PV
            3 : Return to LVM Menu
            4 : Exit Program""")
            pv=input("Enter your choice : ")
            if pv == "1" :
                name=input("Enter the disk name : ")
                os.system("clear")
                os.system("pvcreate " + name)
            elif pv == "2" :
                os.system("clear")
                os.system("pvdisplay")
            elif pv =="3" :
                os.system("clear")
                break
            elif pv == "4" :
                os.system("clear")
                exit()
        elif st == "3" :
          while True :
            print(""" Choose from the options of VG ......
            1 : Create a volume group
            2 : Info about the VG created
            3 : Extend the size of created VG
            4 : Return to LVM Menu
            5 : Exit Program""")
            vg=input("Enter your choice : ")
            if vg == "1" :
                nm = input("Enter the name to be assigned to VG : ")
                part=input("Enter the PVs to be attached (separate by space) : ")
                os.system("clear")
                os.system("vgcreate " + nm + " " + part)
            elif vg == "2" :
                os.system("clear")
                os.system("vgdisplay")
            elif vg == "3" :
                vn = input("Enter the name of VG to extend : ")
                pn = input("Enter the PV to be attached : ")
                os.system("clear")
                os.system("vgextend " + vn + " " + pn)
            elif vg == "4" :
                os.system("clear")
                break
            elif vg == "5" :
                os.system("clear")
                exit()
        elif st == "4" :
          while True :
            print(""" Choose from the options of LV .....
            1 : Create a Logical Volume
            2 : Info about the created LVs
            3 : Extend the size of LV
            4 : Format LV
            5 : Format extended LV
            6 : Mount LV to a driver
            7 : Return to LVM Menu
            8 : Exit Program""")
            lv=input("Enter your choice : ")
            if lv == "1" :
                size=input("Enter the size of partition : ")
                name=input("Enter the name to be allocated : " )
                vna=input("Enter the name of VG to create LV partition : ")
                os.system("clear")
                os.system("lvcreate --size " + size + " --name " + name + " " + vna)
            elif lv == "2" :
                vm=input("Enter the name of VG : ")
                lm=input("Enter the name of LV : ")
                os.system("clear")
                os.system("lvdisplay " + vm + "/" + lm)
            elif lv == "3" :
                es=input("Enter the size required : ")
                lvn=input("Enter the name of LV : ")
                os.system("clear")
                os.system("lvextend --size " + es + " " + lvn)
            elif lv == "4" :
                lvname=input("Enter the name of LV : ")
                os.system("clear")
                os.system("mkfs.ext4 " + lvname)
            elif lv == "5" :
                fes=input("Enter the name of LV : ")
                os.system("clear")
                os.system("resize2fs " + fes)
            elif lv == "6" :
                lvne=input("Enter the name of LV : ")
                dr=input("Enter the path of driver : ")
                os.system("clear")
                os.system("mount " + lvne + " " + dr)
            elif lv == "7" :
                os.system("clear")
                break
            elif lv == "8" :
                os.system("clear")
                exit()
        elif st == "5" :
          os.system("clear")
          break
        elif st == "6" :
          os.system("clear")
          exit()

  elif choice =="4" :
      master_ip = input("\tEnter the IP Address for Master node : ")
      password =getpass.getpass("\tEnter password : ")
      ins = input("do you want to install hadoop to this node? (Y/N) :")
      if ins == "Y" :
        subprocess.getoutput("sshpass -p " + password + "scp /root/hadoop-1.2.1-1.x86_64.rpm " + master_ip + ":/root/")
        subprocess.getoutput("sshpass -p " + password + "scp /root/jdk-8u171-linux-x64.rpm " + master_ip + ":/root/")
        os.system("sshpass -p " + password + "ssh " + master_ip + "rpm -ivh /root/jdk-8u171-linux-x64.rpm ")
        os.system("sshpass -p " + password + "ssh " + master_ip + "rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force ")
      if ins == "Y" or ins == "N":
        print("configuring "+ master_ip + " as master node....")
        os.system("sshpass -p " + password + " ssh " + master_ip + " mkdir /hadoop_namenode_storage")
        subprocess.getoutput("sshpass -p " + password + " scp /etc/hadoop/hdfs-site.xml " +     master_ip + ":/etc/hadoop/hdfs-site.xml")
        subprocess.getoutput("sed -i 's/1.2.3.4/" + master_ip + "/' /etc/hadoop/core-site.xml")
        subprocess.getoutput("sshpass -p " + password + " scp /etc/hadoop/core-site.xml " + master_ip + ":/etc/hadoop/core-site.xml")
        subprocess.getoutput("sed -i 's/" + master_ip + "/1.2.3.4/' /etc/hadoop/core-site.xml")
      print("\n\tMaster node "+ master_ip +" configured successfully ")
      subprocess.getoutput("sshpass -p " + password +" ssh "+ master_ip +"hadoop-daemon.sh start datanode")

      flag = 1
      while(flag == 1):
        print("\n1 : Add slave node to cluster")
        print("2 :  Add hadoop client to cluster")
        print("3 :  Display cluster details (attached nodes)")
        print("4 : Display cluster webUI")
        print("5 : Return to Main Menu")
        print("6 : Exit Program")
        choice= input("Enter your choice:")
        if choice == '1':
                while True:
                        response=input("\nAdd Slave (Y/N):")
                        if response == "Y":
                                slave_ip = input("\tEnter the IP Address for slave node : ")
                                password =getpass.getpass("\tEnter password : ")
                                ins = input("do you want to install hadoop to this node? (Y/N) :")
                                if ins == "Y":
                                        os.system("clear")
                                        subprocess.getoutput("sshpass -p " + password + "scp /root/hadoop-1.2.1-1.x86_64.rpm " + slave_ip + ":/root/")
                                        subprocess.getoutput("sshpass -p " + password + "scp /root/jdk-8u171-linux-x64.rpm " + slave_ip + ":/root/")
                                        os.system("sshpass -p " + password + "ssh " + slave_ip + "rpm -ivh /root/jdk-8u171-linux-x64.rpm ")
                                        os.system("sshpass -p " + password + "ssh " + slave_ip + "rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force ")
                                if ins == "Y" or ins == "N":
                                        os.system("clear")
                                        print("configuring "+ master_ip + " as master node....")
                                        os.system("sshpass -p " + password + " ssh " + slave_ip + " mkdir /hadoop_datanode_storage")
                                        subprocess.getoutput("sshpass -p " + password + " scp /etc/hadoop/hdfs-site.xml " + slave_ip + ":/etc/hadoop/hdfs-site.xml")
                                        subprocess.getoutput("sed -i 's/1.2.3.4/" + slave_ip + "/' /etc/hadoop/core-site.xml")
                                        subprocess.getoutput("sshpass -p " + password + " scp /etc/hadoop/core-site.xml " + slave_ip + ":/etc/hadoop/core-site.xml")
                                        subprocess.getoutput("sed -i 's/" + slave_ip + "/1.2.3.4/' /etc/hadoop/core-site.xml")
                                        subprocess.getoutput("sshpass -p " + password + " ssh "+ slave_ip +"hadoop-daemon.sh start datanode")
                        elif response == "N":
                                os.system("clear")
                                flag=1
                                break
                        else:
                                os.system("clear")
                                print("Enter valid input (either Y or N only)...")
                        print("\n\tSlave node "+ slave_ip + " configured successfully " )


        elif choice == '2':
                client_ip = input("\tEnter the IP Address for Master node : ")
                password =getpass.getpass("\tEnter password : ")
                ins = input("do you want to install hadoop to this node? (Y/N) :")
                if ins == "Y":
                        subprocess.getoutput("sshpass -p " + password + "scp /root/hadoop-1.2.1-1.x86_64.rpm " + client_ip + ":/root/")
                        subprocess.getoutput("sshpass -p " + password + "scp /root/jdk-8u171-linux-x64.rpm " + client_ip + ":/root/")
                        os.system("sshpass -p " + password + "ssh " + client_ip + "rpm -ivh /root/jdk-8u171-linux-x64.rpm ")
                        os.system("sshpass -p " + password + "ssh " + client_ip + "rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force ")
                if ins == "Y" or ins == "N":
                        print("configuring "+ master_ip + " as master node....")
                        subprocess.getoutput("sed -i 's/1.2.3.4/" + master_ip + "/' /etc/hadoop/core-site.xml")
                        subprocess.getoutput("sshpass -p " + password + " scp /etc/hadoop/core-site.xml " + client_ip + ":/etc/hadoop/core-site.xml")
                        subprocess.getoutput("sed -i 's/" + master_ip + "/1.2.3.4/' /etc/hadoop/core-site.xml")
                        print("\n\t Hadoop client "+ client_ip +" configured successfully ")
                        subprocess.getoutput("sshpass -p " + password + " ssh "+ master_ip +"hadoop-daemon.sh start datanode")


        elif choice == '3':
                os.system("clear")
                os.system("sshpass -p " + password + " ssh "+ master_ip +"hadoop dfsadmin --report")
        elif choice == '4':
                os.system("clear")
                wb.open("http://"+ master_ip + ":50070")

        elif choice == '5':
                os.system("clear")
                break
        elif choice == "6" :
                os.system("clear")
                exit()
        else :
                os.system("clear")
                print("Unsupported option chosen")



  elif choice == '8' :
    os.system("clear")
    exit()
  elif choice == '6' :
    while True :
      print("""Choose from the choices below
        1 : Execute custom commands
        2 : Get specialized CLI
        3 : Return to Main Menu
        4 : Exit the program""")
      code = input("Enter your choice : ")
      if code == "1" :
        command = input("Enter the command to be executed : ")
        os.system("clear")
        os.system(command)
      elif code == "2" :
        print("exit to leave")
        while True:
          cmd=input("=>")
          if cmd == "exit":
            os.system("clear")
            break
          else :
            os.system(cmd)
      elif code == "3" :
        os.system("clear")
        break
      elif code == "4" :
        os.system("clear")
        exit()
      else :
        os.system("clear")
        print("Enter a valid option")
  elif choice == "7" :
      while True :
        print(""" Choose from the options below from WEBSERVER........
        1 : Install apache webserver
        2 : Create content
        3 : View the content on browser
        4 : Return to Main Menu
        5 : Exit Program""")
        web=input("Enter your choice : ")
        if web == "1" :
          os.system("clear")
          os.system("yum install httpd -y")
          os.system("systemctl start httpd")
        elif web =="2" :
          p = input("Enter the content to be displayed : ")
          os.system("echo {} >> /var/www/html/index.html".format(p))
        elif web == "3" :
          ip=subprocess.getoutput("hostname -I | awk '{print $1}'")
          os.system("clear")
          print("Redirecting.....")
          wb.open("http://" + ip + ":80")

        elif web == "4" :
          os.system("clear")
          break
        elif web == "5" :
          os.system("clear")
          exit()
        else :
            os.system("clear")
            print("Enter a valid option")


  else  :
    os.sytem("clear")
    print("Enter a valid option")








