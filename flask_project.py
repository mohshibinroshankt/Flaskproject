from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'title': 'My First Blog Post',
        'author': 'John Doe',
        'date': 'January 1, 2023',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan magna ac eros posuere, '
                   'vel semper arcu hendrerit. Integer fringilla euismod enim ut tempus. Sed quis neque sit amet '
                   'libero ' 'vehicula interdum. Duis auctor est eu risus volutpat, non maximus metus facilisis. '
                   'Donec malesuada ' 'volutpat lacus nec gravida. Integer in elit in mi feugiat dapibus at sed sapien.'
                   ' Fusce euismod, ''magna et pretium bibendum, arcu nisl finibus mi, vel molestie magna quam ac'
                   ' nulla. Fusce eget posuere ' 'lacus.'
    },
    {
        'title': 'My Second Blog Post',
        'author': 'Jane Doe',
        'date': 'February 1, 2023',
        'content': 'Suspendisse aliquam lorem ac convallis pulvinar. Nam mattis mauris a augue posuere bibendum.'
                   ' Duis dapibus neque in nisl malesuada fermentum. Suspendisse vitae augue bibendum, volutpat diam '
                   'eget, dapibus metus. Sed in est vel nibh sodales iaculis. Suspendisse fermentum maximus mauris,'
                   ' eget bibendum neque lobortis non. Donec rutrum fermentum arcu, vel congue sapien pharetra eget.'
                   ' Donec id velit sit amet urna porttitor viverra.'
    }
]

chakkas = [
    {
        'title': 'Award 1',
        'description': 'This is the description of award 1.',
        'date': 'January 1, 2023'
    },
    {
        'title': 'Award 2',
        'description': 'This is the description of award 2.',
        'date': 'February 1, 2023'
    },
    {
        'title': 'Award 3',
        'description': 'This is the description of award 3.',
        'date': 'March 1, 2023'
    }
]


pdcts = [
    {
        'name': 'Product 1',
        'description': 'Description of Product 1 goes here',
        'link': '#'
    },
    {
        'name': 'Product 2',
        'description': 'Description of Product 2 goes here',
        'link': '#'
    },
    {
        'name': 'Product 3',
        'description': 'Description of Product 3 goes here',
        'link': '#'
    }
]


@app.route('/')
def index():
    return render_template('index.jinja2')


@app.route('/products')
def products():
    return render_template('products.jinja2', pdcts=pdcts)


@app.route('/services')
def services():
    return render_template('services.jinja2')


@app.route('/customer-service')
def customer_service():
    return render_template('customer_service.jinja2')


@app.route('/testimonials')
def testimonials():
    testimonials = [
        {
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                       'Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue'
                       ' ligula ac quam viverra nec consectetur ante hendrerit.',
            'author': 'John Doe'},
        {
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                       ' Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue '
                       'ligula ac quam viverra nec consectetur ante hendrerit.',
            'author': 'Jane Doe'},
        {
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                       'Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue '
                       'ligula ac quam viverra nec consectetur ante hendrerit.',
            'author': 'Bob Smith'},
    ]
    return render_template('testimonials.jinja2', testimonials=testimonials)


@app.route('/contact')
def contact():
    return render_template('contact.jinja2')


@app.route('/blog')
def blog():
    return render_template('blog.jinja2', title='Blog', posts=posts)


@app.route('/achievements')
def achievements():
    return render_template('achievements.jinja2', title='Achievements', chakkas=chakkas)


if __name__ == "__main__":
    app.run(debug=True)
