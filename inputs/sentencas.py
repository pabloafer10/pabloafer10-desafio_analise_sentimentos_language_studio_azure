import random

# Lista de sentenças
sentencas = [
    "Como utilizo a API do Azure Cognitive Services para processar linguagem natural e entender melhor os textos enviados pelo usuário?",
    "Utilizando a integração com serviços de IA como permitir que meu projeto reconheça padrões e extraía insights automaticamente?",
    "Utilizando a inteligência artificial, como implementar um chatbot que responde perguntas de forma contextualizada e inteligente?",
    "Como faço para explorar a API do Language Studio para analisar sentimentos em textos e entender o tom das mensagens enviadas pelos usuários?",
    "Posso utilizar o Speech-to-Text da Microsoft na automação de processos baseados em voz.",
    "O uso de IA em projetos facilitam a personalização da experiência do usuário, tornando-a mais dinâmica e interativa? Por quê?",
    "Consigo com uso de IA, traduzir textos automaticamente e expandir a acessibilidade do meu projeto para múltiplos idiomas?",
    "É possível integrar modelos de Machine Learning na nuvem para automatizar a classificação de dados de entrada no sistema?",
    "Como consumir APIs de IA diretamente do Python, tornando projetos mais inteligentes e eficientes?",
    "Ferramentas de IA podem ser integradas a sistemas existentes, facilitando a adoção sem grandes mudanças na infraestrutura?",
    "Utilizar a análise preditiva, é uma forma de impulsionar através de IA empresas a antecipar tendências e comportamentos do mercado?",
    "A integração de IA em plataformas de e-commerce é uma ferramenta poderosa para otimizar e recomendar produtos para os consumidores?",
    "Devo utilizar sistemas para monitorar e melhorar a segurança cibernética em tempo real?",
    "É necessário a colaboração entre humanos para que as máquinas utilizando integração de serviços de IA, resultem em melhores tomadas de decisões?",
    "A implementação de IA em processos de negócios pode levar a uma significativa redução de custos e aumento de produtividade?"
]

# Função para exibir uma sentença aleatória
def exibir_sentenca():
    sentenca = random.choice(sentencas)
    print(sentenca)

# Executar a função
exibir_sentenca()