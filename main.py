#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.abspath('./Modules/'))

import DevNux

DevNux 	= DevNux()

while True:

	DevNux.clear()
	print('########### INSTALAR SETUP - DESENVLVIMENTO WEB ###########')
	print('\n')
	print('1) Instalar')
	print('2) Ativar Modulos')
	print('3) Verificar oque está instalado')
	print('0) Sair')

	acao = input('')

	if acao == '1':

		DevNux.clear()
		print("\n--------------- atualizando os pacotes")
		os.system('sudo apt-get update && sudo apt-get upgrade -y')

		print("\n--------------- adicionando o repositório do postgresql")
		os.system('sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -')

		print("\n--------------- adicionando mais paradas do postgresql")
		os.system('sudo sh -c \'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list\'')

		print("\n--------------- adicionando o repositório do PHP")
		os.system('sudo add-apt-repository ppa:ondrej/php -y')

		print("\n--------------- adicionando o repositório do Sublime Text")
		os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list -y')

		print("\n--------------- instalando o Apache2, PHP 7.4, Postgre, Sublime Text e o módulo PDO")
		os.system('sudo apt install apache2 php7.4 php7.4-pgsql postgresql postgresql-contrib pgadmin4 pgadmin4-apache2 sublime-text -y')

		print("\n--------------- instalando PG Admin 4")
		os.system('sudo apt-get install wget ca-certificates -y')

		print("\n--------------- reiniciando o apache")
		os.system('sudo service apache2 restart')

		print('\n--------------- pronto, foi tudo instalado.')
		input()

	if acao == '2':

		DevNux.clear()
		print("\n--------------- ativando a escrita no .htacess")
		os.system('sudo a2enmod rewrite')

		print("\n--------------- ativando a escrita dos headers")
		os.system('sudo a2enmod headers')

		print("\n--------------- ativando o cache")
		os.system('sudo a2enmod expires')

		print("\n--------------- ativando o SSL")
		os.system('sudo a2enmod ssl')

		print("\n--------------- reiniciando o apache")
		os.system('sudo service apache2 restart')

		print('\n-------------- pronto, os modulos foram ativados.')
		input()

	if acao == '3':

		DevNux.clear()
		print('\n\n-------------- verificando PHP\n')
		os.system('php --version')

		print('\n\n-------------- verificando apache2\n')
		os.system('apache2 -v')

		print('\n\n-------------- verificando postgre SQL\n')
		os.system('service postgresql status')

		print('\n\n-------------- verificando sublime-text\n')
		os.system('sublime-text.subl --version')

		print('\n\n-------------- pronto, todos os programas verificados.\n')
		input()

	if acao == '0':
		DevNux.clear()
		print('Até logo.. :*')
		break

	DevNux.clear()
